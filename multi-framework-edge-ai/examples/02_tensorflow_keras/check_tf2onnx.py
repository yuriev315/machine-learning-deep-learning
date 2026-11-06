#!/usr/bin/env python3
"""Checks the tf2onnx output with ONNX Runtime on the shared test set. Keeps TF's NHWC input layout."""
import os, sys
import onnxruntime as ort
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "common"))
from pyeval import load, evaluate
_, _, xte, yte = load(); p = os.path.join(H, "..", "artifacts", "tensorflow", "tinycnn_tf2onnx.onnx")
so = ort.SessionOptions(); so.intra_op_num_threads = 1; s = ort.InferenceSession(p, so, providers=["CPUExecutionProvider"]); n = s.get_inputs()[0].name
evaluate("tf_tf2onnx_ort_py", lambda x: s.run(None, {n: x[None, ..., None]})[0][0], xte, yte, p)
