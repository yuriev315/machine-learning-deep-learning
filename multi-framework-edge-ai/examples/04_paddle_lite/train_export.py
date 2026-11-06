#!/usr/bin/env python3
"""Project 04: PaddlePaddle 3.0 training -> .pdparams -> inference model (legacy .pdmodel and PIR .json) -> Paddle Inference -> ONNX via paddle2onnx."""
import os, sys, warnings
warnings.simplefilter("ignore")
H = os.path.dirname(os.path.abspath(__file__)); A = os.path.join(H, "..", "artifacts", "paddle"); os.makedirs(A, exist_ok=True); sys.path.insert(0, os.path.join(H, "..", "common"))
mode = sys.argv[1] if len(sys.argv) > 1 else "train"
os.environ["FLAGS_enable_pir_api"] = "0" if mode == "legacy" else "1"   # .pdmodel for Paddle Lite 2.12, PIR for current tooling
import numpy as np, paddle, paddle.nn as nn
from pyeval import load, evaluate
paddle.seed(20250601); np.random.seed(20250601); paddle.set_device("cpu")
xtr, ytr, xte, yte = load()
class TinyCNN(nn.Layer):
    def __init__(self):
        super().__init__()
        self.c1 = nn.Conv2D(1, 8, 3, padding=1); self.c2 = nn.Conv2D(8, 16, 3, padding=1); self.p = nn.MaxPool2D(2); self.r = nn.ReLU(); self.fc = nn.Linear(64, 10)
    def forward(self, x):  # to_static needs the first argument to be named self
        x = self.p(self.r(self.c2(self.p(self.r(self.c1(x))))))
        return self.fc(paddle.flatten(x, 1))
m = TinyCNN(); ck = os.path.join(A, "tinycnn.pdparams")
if mode == "train":
    opt = paddle.optimizer.Adam(3e-3, parameters=m.parameters()); L = nn.CrossEntropyLoss(); X, Y = paddle.to_tensor(xtr[:, None]), paddle.to_tensor(ytr)
    for ep in range(40):
        pm = np.random.permutation(len(xtr))
        for i in range(0, len(pm), 64):
            b = paddle.to_tensor(pm[i:i + 64]); opt.clear_grad(); L(m(X[b]), Y[b]).backward(); opt.step()
    paddle.save(m.state_dict(), ck)
m.set_state_dict(paddle.load(ck)); m.eval()
print("mode", mode, "pir", os.environ["FLAGS_enable_pir_api"], "accuracy", float((m(paddle.to_tensor(xte[:, None])).numpy().argmax(1) == yte).mean()))
stem = os.path.join(A, "legacy" if mode == "legacy" else "pir", "tinycnn")
paddle.jit.save(paddle.jit.to_static(m, input_spec=[paddle.static.InputSpec([None, 1, 8, 8], "float32", "input")], full_graph=True), stem)
print(sorted(os.listdir(os.path.dirname(stem))))
if mode == "train":
    from paddle.inference import Config, create_predictor
    c = Config(stem + ".json", stem + ".pdiparams"); c.disable_gpu(); c.set_cpu_math_library_num_threads(1); p = create_predictor(c)
    i, o = p.get_input_handle(p.get_input_names()[0]), p.get_output_handle(p.get_output_names()[0])
    def run(x):
        i.reshape([1, 1, 8, 8]); i.copy_from_cpu(x[None, None]); p.run(); return o.copy_to_cpu()[0]
    evaluate("paddle_inference_py", run, xte, yte, stem + ".pdiparams")
