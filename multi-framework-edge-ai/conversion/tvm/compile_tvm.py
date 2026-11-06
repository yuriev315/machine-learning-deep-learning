#!/usr/bin/env python3
"""ONNX -> Apache TVM Relax -> compiled shared module for x86-64 -> Python runtime."""
import os, sys, warnings
warnings.simplefilter("ignore")
import numpy as np, onnx, tvm
from tvm import relax
from tvm.relax.frontend.onnx import from_onnx
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, os.path.join(R, "examples", "common"))
from pyeval import load, evaluate
A = os.path.join(R, "examples", "artifacts"); OUT = os.path.join(A, "tvm"); os.makedirs(OUT, exist_ok=True)
xtr, ytr, xte, yte = load()
mod = from_onnx(onnx.load(os.path.join(A, "pytorch", "tinycnn.onnx")), shape_dict={"input": [1, 1, 8, 8]}, keep_params_in_input=False)
print("tvm", tvm.__version__)
ex = relax.build(mod, target=tvm.target.Target("llvm", host="llvm"))
so = os.path.join(OUT, "tinycnn_x86_64.so"); ex.mod.export_library(so) if hasattr(ex, "mod") else None
vm = relax.VirtualMachine(ex, tvm.cpu())
evaluate("pytorch_onnx_tvm_py", lambda x: vm["main"](tvm.runtime.tensor(x[None, None])).numpy()[0], xte, yte, so if os.path.exists(so) else None)
