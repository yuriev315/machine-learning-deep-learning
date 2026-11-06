#!/usr/bin/env python3
"""Project 01: PyTorch training -> checkpoint -> TorchScript / .pt2 / ONNX -> inference and output-equality checks."""
import os, sys, warnings
import numpy as np, torch, torch.nn as nn
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
from pyeval import load, evaluate
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts", "pytorch"); os.makedirs(OUT, exist_ok=True)
torch.manual_seed(20250601); torch.set_num_threads(1)
class TinyCNN(nn.Module):
    """NCHW 1x8x8 -> 10 logits. Small enough to run on a Cortex-M."""
    def __init__(s):
        super().__init__()
        s.features = nn.Sequential(nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2))
        s.fc = nn.Linear(64, 10)
    def forward(s, x):
        return s.fc(torch.flatten(s.features(x), 1))
if __name__ == "__main__":
    xtr, ytr, xte, yte = load()
    X, Y = torch.from_numpy(xtr[:, None]), torch.from_numpy(ytr)
    m = TinyCNN(); opt = torch.optim.Adam(m.parameters(), 3e-3); loss = nn.CrossEntropyLoss()
    for ep in range(40):
        p = torch.randperm(len(X))
        for i in range(0, len(X), 64):
            b = p[i:i + 64]; opt.zero_grad(); loss(m(X[b]), Y[b]).backward(); opt.step()
    m.eval()
    ck = os.path.join(OUT, "tinycnn.pth"); torch.save({"state_dict": m.state_dict(), "epoch": 40}, ck)
    m2 = TinyCNN(); m2.load_state_dict(torch.load(ck, weights_only=True)["state_dict"]); m2.eval()    # checkpoint round trip
    ex = torch.zeros(1, 1, 8, 8)
    ts = torch.jit.trace(m2, ex); ts.save(os.path.join(OUT, "tinycnn.torchscript.pt"))
    ep = torch.export.export(m2, (ex,)); torch.export.save(ep, os.path.join(OUT, "tinycnn.pt2"))
    onx = os.path.join(OUT, "tinycnn.onnx")
    torch.onnx.export(m2, ex, onx, opset_version=17, input_names=["input"], output_names=["logits"], dynamic_axes={"input": {0: "batch"}, "logits": {0: "batch"}}, dynamo=False)
    import onnx, onnxruntime as ort
    onnx.checker.check_model(onnx.load(onx))
    so = ort.SessionOptions(); so.intra_op_num_threads = 1
    s = ort.InferenceSession(onx, so, providers=["CPUExecutionProvider"])
    with torch.no_grad():
        ref = m2(torch.from_numpy(xte[:, None])).numpy()
        tsv = ts(torch.from_numpy(xte[:, None])).numpy(); pt2 = torch.export.load(os.path.join(OUT, "tinycnn.pt2")).module(); ep2 = np.concatenate([pt2(torch.from_numpy(x[None, None])).numpy() for x in xte])
    ov = s.run(None, {"input": xte[:, None]})[0]
    print("max|torch-torchscript|", np.abs(ref - tsv).max(), "max|torch-pt2|", np.abs(ref - ep2).max(), "max|torch-onnxruntime|", np.abs(ref - ov).max())
    np.save(os.path.join(OUT, "reference_logits.npy"), ref)
    def pred(x):
        with torch.no_grad():
            return m2(torch.from_numpy(x[None, None]))[0].numpy()
    evaluate("pytorch_eager_py", pred, xte, yte, ck)
    evaluate("torchscript_py", lambda x: ts(torch.from_numpy(x[None, None]))[0].detach().numpy(), xte, yte, os.path.join(OUT, "tinycnn.torchscript.pt"))
    evaluate("onnxruntime_py", lambda x: s.run(None, {"input": x[None, None]})[0][0], xte, yte, onx)
