#!/usr/bin/env python3
"""Project 04b: MindSpore 2.7.2 training -> .ckpt -> MINDIR and ONNX export."""
import os, warnings
warnings.simplefilter("ignore")
import numpy as np, mindspore as ms
from mindspore import nn, Tensor
ms.set_context(mode=ms.GRAPH_MODE, device_target="CPU"); ms.set_seed(20250601); np.random.seed(20250601)
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "..", "artifacts", "mindspore"); os.makedirs(OUT, exist_ok=True)
d = np.load(os.path.join(H, "..", "data", "digits.npz")); xtr, ytr, xte, yte = d["x_train"][:, None], d["y_train"].astype(np.int32), d["x_test"][:, None], d["y_test"]
class TinyCNN(nn.Cell):
    def __init__(self):
        super().__init__()
        self.c1 = nn.Conv2d(1, 8, 3, pad_mode="same", has_bias=True); self.c2 = nn.Conv2d(8, 16, 3, pad_mode="same", has_bias=True)
        self.r = nn.ReLU(); self.p = nn.MaxPool2d(2, 2); self.f = nn.Flatten(); self.fc = nn.Dense(64, 10)
    def construct(self, x):
        return self.fc(self.f(self.p(self.r(self.c2(self.p(self.r(self.c1(x))))))))
n = TinyCNN()
opt = nn.Adam(n.trainable_params(), learning_rate=3e-3)
loss = nn.SoftmaxCrossEntropyWithLogits(sparse=True, reduction="mean")
step = nn.TrainOneStepCell(nn.WithLossCell(n, loss), opt); step.set_train()
for ep in range(40):
    p = np.random.permutation(len(xtr))
    for i in range(0, len(p) - 63, 64):
        b = p[i:i + 64]; step(Tensor(xtr[b], ms.float32), Tensor(ytr[b], ms.int32))
n.set_train(False)
pr = n(Tensor(xte, ms.float32)).asnumpy(); print("mindspore accuracy", (pr.argmax(1) == yte).mean())
ck = os.path.join(OUT, "tinycnn.ckpt"); ms.save_checkpoint(n, ck)
n2 = TinyCNN(); ms.load_param_into_net(n2, ms.load_checkpoint(ck)); n2.set_train(False)
print("checkpoint reload max diff", float(np.abs(n2(Tensor(xte, ms.float32)).asnumpy() - pr).max()))
ex = Tensor(np.zeros((1, 1, 8, 8), np.float32))
ms.export(n2, ex, file_name=os.path.join(OUT, "tinycnn"), file_format="MINDIR")
try:
    ms.export(n2, ex, file_name=os.path.join(OUT, "tinycnn"), file_format="ONNX"); print("onnx export ok")
except Exception as e:
    print("onnx export failed:", type(e).__name__, str(e)[:200])
print({f: os.path.getsize(os.path.join(OUT, f)) for f in sorted(os.listdir(OUT))})
