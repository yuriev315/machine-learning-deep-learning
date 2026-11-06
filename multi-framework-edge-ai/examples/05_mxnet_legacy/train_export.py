#!/usr/bin/env python3
"""Project 05 (legacy env): MXNet 1.9.1 Gluon training -> Symbol JSON + params -> reload -> mx2onnx.
Apache MXNet was retired to the Apache Attic in 2023. Historical use only; not maintained."""
import json, os, warnings
warnings.simplefilter("ignore")
import numpy as np, mxnet as mx
from mxnet import gluon, autograd
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "..", "artifacts", "mxnet"); os.makedirs(OUT, exist_ok=True)
d = np.load(os.path.join(H, "..", "data", "digits.npz")); xtr, ytr, xte, yte = d["x_train"][:, None], d["y_train"], d["x_test"][:, None], d["y_test"]
mx.random.seed(20250601); np.random.seed(20250601)
n = gluon.nn.HybridSequential()
n.add(gluon.nn.Conv2D(8, 3, padding=1, activation="relu"), gluon.nn.MaxPool2D(2), gluon.nn.Conv2D(16, 3, padding=1, activation="relu"), gluon.nn.MaxPool2D(2), gluon.nn.Flatten(), gluon.nn.Dense(10))
n.initialize(mx.init.Xavier()); n.hybridize()
tr = gluon.Trainer(n.collect_params(), "adam", {"learning_rate": 3e-3}); L = gluon.loss.SoftmaxCrossEntropyLoss()
for ep in range(40):
    p = np.random.permutation(len(xtr))
    for i in range(0, len(p), 64):
        b = p[i:i + 64]; X, Y = mx.nd.array(xtr[b]), mx.nd.array(ytr[b])
        with autograd.record():
            l = L(n(X), Y)
        l.backward(); tr.step(len(b))
pred = n(mx.nd.array(xte)).asnumpy(); print("gluon accuracy", (pred.argmax(1) == yte).mean())
n.export(os.path.join(OUT, "tinycnn"), epoch=0)
sb = gluon.nn.SymbolBlock.imports(os.path.join(OUT, "tinycnn-symbol.json"), ["data"], os.path.join(OUT, "tinycnn-0000.params"))
re = sb(mx.nd.array(xte)).asnumpy(); print("reload max diff", float(np.abs(re - pred).max()), "accuracy", (re.argmax(1) == yte).mean())
np.save(os.path.join(OUT, "reference_logits.npy"), pred)
onx = os.path.join(OUT, "tinycnn.onnx")
mx.onnx.export_model(os.path.join(OUT, "tinycnn-symbol.json"), os.path.join(OUT, "tinycnn-0000.params"), [(1, 1, 8, 8)], [np.float32], onx)
print("sizes", {f: os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT)})
