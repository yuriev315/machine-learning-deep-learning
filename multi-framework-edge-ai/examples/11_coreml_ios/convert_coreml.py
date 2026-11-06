#!/usr/bin/env python3
"""Project 11: PyTorch -> Core ML mlprogram (.mlpackage), float16 weights and INT8 weights.
Conversion runs on Linux. Real prediction needs macOS/iOS: coremltools has no Core ML runtime here.
As a substitute, a small independent interpreter below executes the converted MIL program (its ops and stored weights) with NumPy/PyTorch on the
shared test set. That checks the converted graph and weights. It does not exercise the Core ML runtime or the Neural Engine."""
import logging, os, sys, warnings
warnings.simplefilter("ignore"); logging.disable(logging.WARNING)
import torch, coremltools as ct
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "01_pytorch"))
from train_export import TinyCNN
A = os.path.join(H, "..", "artifacts"); OUT = os.path.join(A, "coreml"); os.makedirs(OUT, exist_ok=True)
m = TinyCNN(); m.load_state_dict(torch.load(os.path.join(A, "pytorch", "tinycnn.pth"), weights_only=True)["state_dict"]); m.eval()
ts = torch.jit.trace(m, torch.zeros(1, 1, 8, 8))
ml = ct.convert(ts, inputs=[ct.TensorType(name="input", shape=(1, 1, 8, 8))], outputs=[ct.TensorType(name="logits")], convert_to="mlprogram", minimum_deployment_target=ct.target.iOS16, compute_precision=ct.precision.FLOAT16)
ml.save(os.path.join(OUT, "TinyCNN.mlpackage"))
import coremltools.optimize.coreml as cto
q = cto.linear_quantize_weights(ml, config=cto.OptimizationConfig(global_config=cto.OpLinearQuantizerConfig(mode="linear_symmetric", dtype="int8")))
q.save(os.path.join(OUT, "TinyCNN_int8.mlpackage"))
print("spec ops:", sorted({o.type for f in ml.get_spec().mlProgram.functions.values() for o in f.block_specializations[list(f.block_specializations)[0]].operations})[:14])
import numpy as np, torch.nn.functional as F
sys.path.insert(0, os.path.join(H, "..", "common"))
from pyeval import load, evaluate
_, _, xte, yte = load()
def run_mil(prog, x):
    env = {"input": torch.from_numpy(x[None, None])}
    def val(v):
        if v is None: return None
        if v.name in env: return env[v.name]
        return v.val
    fn = prog.functions["main"]
    for op in fn.operations:
        I = {k: (val(v) if not isinstance(v, (list, tuple)) else [val(q) for q in v]) for k, v in op.inputs.items()}
        t = op.op_type
        if t == "const": r = op.outputs[0].val
        elif t == "constexpr_affine_dequantize":
            q = np.asarray(op.quantized_data.val, np.float32); zp = np.asarray(op.zero_point.val, np.float32); sc = np.asarray(op.scale.val, np.float32); ax = int(op.axis.val)
            sh = [1] * q.ndim
            if sc.ndim: sh[ax] = -1
            r = (q - zp.reshape(sh)) * sc.reshape(sh)
        elif t == "cast": r = torch.as_tensor(I["x"])
        elif t == "conv":
            p = np.asarray(I["pad"]).tolist(); w = torch.as_tensor(np.asarray(I["weight"], np.float32)); b = I.get("bias")
            xx = F.pad(torch.as_tensor(I["x"]).float(), (p[2], p[3], p[0], p[1]))
            r = F.conv2d(xx, w, None if b is None else torch.as_tensor(np.asarray(b, np.float32)), tuple(np.asarray(I["strides"]).tolist()), 0, tuple(np.asarray(I["dilations"]).tolist()), int(I["groups"]))
        elif t == "relu": r = F.relu(torch.as_tensor(I["x"]))
        elif t == "max_pool": r = F.max_pool2d(torch.as_tensor(I["x"]), tuple(np.asarray(I["kernel_sizes"]).tolist()), tuple(np.asarray(I["strides"]).tolist()))
        elif t == "reshape": r = torch.as_tensor(I["x"]).reshape(tuple(int(v) for v in np.asarray(I["shape"]).tolist()))
        elif t == "linear": r = F.linear(torch.as_tensor(I["x"]), torch.as_tensor(np.asarray(I["weight"], np.float32)), None if I.get("bias") is None else torch.as_tensor(np.asarray(I["bias"], np.float32)))
        else: raise NotImplementedError(t)
        env[op.outputs[0].name] = r if isinstance(r, torch.Tensor) else r
    return env[fn.outputs[0].name].numpy()[0]
evaluate("pytorch_coreml_fp16_mil_interpreter_py", lambda x: run_mil(ml._mil_program, x), xte, yte, size=os.path.getsize(os.path.join(OUT, "TinyCNN.mlpackage", "Data", "com.apple.CoreML", "weights", "weight.bin")))
evaluate("pytorch_coreml_int8_mil_interpreter_py", lambda x: run_mil(q._mil_program, x), xte, yte, size=os.path.getsize(os.path.join(OUT, "TinyCNN_int8.mlpackage", "Data", "com.apple.CoreML", "weights", "weight.bin")))
