#!/usr/bin/env python3
"""Project 14: ONNX -> RKNN (INT8, RK3588) with RKNN-Toolkit2 2.3.2. Accuracy is measured on the toolkit's x86 simulator, NOT on an NPU."""
import os, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "common"))
from pyeval import load, evaluate
from rknn.api import RKNN
A = os.path.join(H, "..", "artifacts"); OUT = os.path.join(A, "rknn"); os.makedirs(OUT, exist_ok=True)
xtr, ytr, xte, yte = load()
cal = os.path.join(OUT, "calib"); os.makedirs(cal, exist_ok=True); lst = os.path.join(OUT, "dataset.txt")
with open(lst, "w") as f:
    for i, x in enumerate(xtr[:100]):
        p = os.path.abspath(os.path.join(cal, f"{i}.npy")); np.save(p, x[None].astype(np.float32)); f.write(p + "\n")   # 1,8,8 CHW -> toolkit expects NHWC/NCHW per data_format
r = RKNN(verbose=False)
assert r.config(target_platform="rk3588", optimization_level=2) == 0
assert r.load_onnx(os.path.join(A, "pytorch", "tinycnn.onnx"), inputs=["input"], input_size_list=[[1, 1, 8, 8]]) == 0
assert r.build(do_quantization=True, dataset=lst) == 0
pth = os.path.join(OUT, "tinycnn_rk3588_int8.rknn"); assert r.export_rknn(pth) == 0
assert r.init_runtime() == 0   # no target: x86 simulator
evaluate("pytorch_onnx_rknn_int8_simulator_py", lambda x: r.inference(inputs=[x[None, None]], data_format="nchw")[0][0], xte, yte, pth)
r.release()
