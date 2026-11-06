#!/usr/bin/env python3
"""Project 18: quantization comparison, measured on the shared test set.
ONNX Runtime dynamic and static QDQ (per-tensor, per-channel) INT8 + float16; OpenVINO NNCF INT8 post-training; PyTorch QAT -> ONNX INT8.
TFLite, ExecuTorch and MNN results come from their own projects. Everything lands in manifests/quant_comparison.csv."""
import os, sys, warnings
warnings.simplefilter("ignore")
import numpy as np, onnx, onnxruntime as ort
from onnxruntime.quantization import quantize_dynamic, quantize_static, CalibrationDataReader, QuantType, QuantFormat
from onnxruntime.quantization.shape_inference import quant_pre_process
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "common"), os.path.join(H, "..", "01_pytorch")]
from pyeval import load, evaluate
A = os.path.join(H, "..", "artifacts"); OUT = os.path.join(A, "quant"); os.makedirs(OUT, exist_ok=True)
xtr, ytr, xte, yte = load(); src = os.path.join(A, "pytorch", "tinycnn.onnx")
pre = os.path.join(OUT, "tinycnn_pre.onnx"); quant_pre_process(src, pre)
def score(route, path):
    so = ort.SessionOptions(); so.intra_op_num_threads = 1
    s = ort.InferenceSession(path, so, providers=["CPUExecutionProvider"]); n = s.get_inputs()[0].name
    return evaluate(route, lambda x: s.run(None, {n: x[None, None]})[0][0], xte, yte, path)
class R(CalibrationDataReader):
    def __init__(s, n=200): s.i = iter({"input": x[None, None]} for x in xtr[:n])
    def get_next(s): return next(s.i, None)
score("ort_fp32", src)
# ConvInteger only has a CPU kernel for unsigned weights, so QInt8 weights fail at session creation (NOT_IMPLEMENTED).
p = os.path.join(OUT, "dynamic_uint8.onnx"); quantize_dynamic(pre, p, weight_type=QuantType.QUInt8); score("ort_dynamic_uint8", p)
p = os.path.join(OUT, "static_qdq_pertensor.onnx"); quantize_static(pre, p, R(), quant_format=QuantFormat.QDQ, per_channel=False, activation_type=QuantType.QInt8, weight_type=QuantType.QInt8); score("ort_static_int8_pertensor", p)
p = os.path.join(OUT, "static_qdq_perchannel.onnx"); quantize_static(pre, p, R(), quant_format=QuantFormat.QDQ, per_channel=True, activation_type=QuantType.QInt8, weight_type=QuantType.QInt8); score("ort_static_int8_perchannel", p)
from onnxruntime.transformers.float16 import convert_float_to_float16
m16 = convert_float_to_float16(onnx.load(src), keep_io_types=True); p = os.path.join(OUT, "fp16.onnx"); onnx.save(m16, p); score("ort_fp16", p)
# INT4 weights: QDQ with 4-bit weights, ONNX Runtime 1.22 extended quant types
try:
    from onnxruntime.quantization import quantize as q2, StaticQuantConfig
    p = os.path.join(OUT, "static_qdq_int4w.onnx"); quantize_static(pre, p, R(), quant_format=QuantFormat.QDQ, per_channel=True, activation_type=QuantType.QInt8, weight_type=QuantType.QInt4, extra_options={"ActivationSymmetric": False}); score("ort_static_weights_int4", p)
except Exception as e:
    print("INT4 not available:", type(e).__name__, str(e)[:160])
# graph optimization: ORT saves its optimized graph to disk
so = ort.SessionOptions(); so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL; p = os.path.join(OUT, "ort_opt_all.onnx"); so.optimized_model_filepath = p; ort.InferenceSession(src, so, providers=["CPUExecutionProvider"]); print("optimized nodes", len(onnx.load(src).graph.node), "->", len(onnx.load(p).graph.node)); score("ort_fp32_graph_optimized", p)
# ---- OpenVINO NNCF ----
import nncf, openvino as ov
c = ov.Core(); m = c.read_model(os.path.join(A, "openvino", "tinycnn_onnx.xml"))
qm = nncf.quantize(m, nncf.Dataset([x[None, None] for x in xtr[:200]]), subset_size=200, preset=nncf.QuantizationPreset.PERFORMANCE)
xml = os.path.join(A, "openvino", "tinycnn_int8.xml"); ov.save_model(qm, xml)
for route, mdl, path in (("openvino_fp32", m, os.path.join(A, "openvino", "tinycnn_onnx.bin")), ("openvino_nncf_int8", qm, xml[:-3] + "bin")):
    cm = c.compile_model(mdl, "CPU", {"INFERENCE_NUM_THREADS": 1}); rq = cm.create_infer_request()
    evaluate(route, lambda x: rq.infer({0: x[None, None]})[0][0], xte, yte, path)
# ---- PyTorch QAT -> ONNX ----
import torch, torch.nn as nn
from train_export import TinyCNN
from torch.ao.quantization.quantize_fx import prepare_qat_fx, convert_fx
from torch.ao.quantization import get_default_qat_qconfig_mapping
torch.backends.quantized.engine = "fbgemm"; torch.manual_seed(20250601)
fm = TinyCNN(); fm.load_state_dict(torch.load(os.path.join(A, "pytorch", "tinycnn.pth"), weights_only=True)["state_dict"]); fm.train()
ex = (torch.zeros(1, 1, 8, 8),); qat = prepare_qat_fx(fm, get_default_qat_qconfig_mapping("fbgemm"), ex)
opt = torch.optim.Adam(qat.parameters(), 5e-4); L = nn.CrossEntropyLoss(); X, Y = torch.from_numpy(xtr[:, None]), torch.from_numpy(ytr)
for ep in range(8):
    pm = torch.randperm(len(X))
    for i in range(0, len(X), 64):
        b = pm[i:i + 64]; opt.zero_grad(); L(qat(X[b]), Y[b]).backward(); opt.step()
qat.eval(); cvt = convert_fx(qat); ts = torch.jit.trace(cvt, ex[0]); pq = os.path.join(OUT, "qat_fbgemm.torchscript.pt"); ts.save(pq)
with torch.no_grad():
    evaluate("pytorch_qat_fbgemm_int8", lambda x: ts(torch.from_numpy(x[None, None]))[0].numpy(), xte, yte, pq)
