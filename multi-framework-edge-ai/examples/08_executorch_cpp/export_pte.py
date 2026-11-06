#!/usr/bin/env python3
"""Project 08: PyTorch -> torch.export -> Edge -> XNNPACK lowering -> .pte (float32 and INT8 PT2E), checked with the Python runtime."""
import os, sys, warnings
warnings.simplefilter("ignore")
import numpy as np, torch
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "common"), os.path.join(H, "..", "01_pytorch")]
from pyeval import load, evaluate
from train_export import TinyCNN
from executorch.exir import to_edge_transform_and_lower
from executorch.backends.xnnpack.partition.xnnpack_partitioner import XnnpackPartitioner
from executorch.extension.pybindings.portable_lib import _load_for_executorch
A = os.path.join(H, "..", "artifacts"); OUT = os.path.join(A, "executorch"); os.makedirs(OUT, exist_ok=True)
xtr, ytr, xte, yte = load()
m = TinyCNN(); m.load_state_dict(torch.load(os.path.join(A, "pytorch", "tinycnn.pth"), weights_only=True)["state_dict"]); m.eval()
ex = (torch.zeros(1, 1, 8, 8),)
def lower(ep, path):
    prog = to_edge_transform_and_lower(ep, partitioner=[XnnpackPartitioner()]).to_executorch()
    open(path, "wb").write(prog.buffer); return path
def run(route, path):
    rt = _load_for_executorch(path)
    evaluate(route, lambda x: rt.forward([torch.from_numpy(x[None, None])])[0].numpy()[0], xte, yte, path)
fp = lower(torch.export.export(m, ex), os.path.join(OUT, "tinycnn_xnnpack.pte")); run("pytorch_executorch_xnnpack_py", fp)
try:
    from torchao.quantization.pt2e.quantize_pt2e import prepare_pt2e, convert_pt2e
except ImportError:
    from torch.ao.quantization.quantize_pt2e import prepare_pt2e, convert_pt2e
from executorch.backends.xnnpack.quantizer.xnnpack_quantizer import XNNPACKQuantizer, get_symmetric_quantization_config
q = XNNPACKQuantizer().set_global(get_symmetric_quantization_config(is_per_channel=True))
g = torch.export.export_for_training(m, ex).module()
p = prepare_pt2e(g, q)
for x in xtr[:200]:
    p(torch.from_numpy(x[None, None]))
c = convert_pt2e(p)
qp = lower(torch.export.export(c, ex), os.path.join(OUT, "tinycnn_xnnpack_int8.pte")); run("pytorch_executorch_xnnpack_int8_py", qp)
