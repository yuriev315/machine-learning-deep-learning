import os
import numpy as np
import tempfile, zipfile
import torch
import torch.nn as nn
import torch.nn.functional as F
try:
    import torchvision
    import torchaudio
except:
    pass

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()

        self.features_0 = nn.Conv2d(bias=True, dilation=(1,1), groups=1, in_channels=1, kernel_size=(3,3), out_channels=8, padding=(1,1), padding_mode='zeros', stride=(1,1))
        self.features_1 = nn.ReLU()
        self.features_2 = nn.MaxPool2d(ceil_mode=False, dilation=(1,1), kernel_size=(2,2), padding=(0,0), return_indices=False, stride=(2,2))
        self.features_3 = nn.Conv2d(bias=True, dilation=(1,1), groups=1, in_channels=8, kernel_size=(3,3), out_channels=16, padding=(1,1), padding_mode='zeros', stride=(1,1))
        self.features_4 = nn.ReLU()
        self.features_5 = nn.MaxPool2d(ceil_mode=False, dilation=(1,1), kernel_size=(2,2), padding=(0,0), return_indices=False, stride=(2,2))
        self.fc = nn.Linear(bias=True, in_features=64, out_features=10)

        archive = zipfile.ZipFile('tinycnn_pnnx.pnnx.bin', 'r')
        self.features_0.bias = self.load_pnnx_bin_as_parameter(archive, 'features.0.bias', (8), 'float32')
        self.features_0.weight = self.load_pnnx_bin_as_parameter(archive, 'features.0.weight', (8,1,3,3), 'float32')
        self.features_3.bias = self.load_pnnx_bin_as_parameter(archive, 'features.3.bias', (16), 'float32')
        self.features_3.weight = self.load_pnnx_bin_as_parameter(archive, 'features.3.weight', (16,8,3,3), 'float32')
        self.fc.bias = self.load_pnnx_bin_as_parameter(archive, 'fc.bias', (10), 'float32')
        self.fc.weight = self.load_pnnx_bin_as_parameter(archive, 'fc.weight', (10,64), 'float32')
        archive.close()

    def load_pnnx_bin_as_parameter(self, archive, key, shape, dtype, requires_grad=True):
        return nn.Parameter(self.load_pnnx_bin_as_tensor(archive, key, shape, dtype), requires_grad)

    def load_pnnx_bin_as_tensor(self, archive, key, shape, dtype):
        fd, tmppath = tempfile.mkstemp()
        with os.fdopen(fd, 'wb') as tmpf, archive.open(key) as keyfile:
            tmpf.write(keyfile.read())
        m = np.memmap(tmppath, dtype=dtype, mode='r', shape=shape).copy()
        os.remove(tmppath)
        return torch.from_numpy(m)

    def forward(self, v_0):
        v_1 = self.features_0(v_0)
        v_2 = self.features_1(v_1)
        v_3 = self.features_2(v_2)
        v_4 = self.features_3(v_3)
        v_5 = self.features_4(v_4)
        v_6 = self.features_5(v_5)
        v_7 = torch.flatten(input=v_6, end_dim=-1, start_dim=1)
        v_8 = self.fc(v_7)
        return v_8

def export_torchscript():
    net = Model()
    net.float()
    net.eval()

    torch.manual_seed(0)
    v_0 = torch.rand(1, 1, 8, 8, dtype=torch.float)

    mod = torch.jit.trace(net, v_0)
    mod.save("tinycnn_pnnx_pnnx.py.pt")

def export_onnx():
    net = Model()
    net.float()
    net.eval()

    torch.manual_seed(0)
    v_0 = torch.rand(1, 1, 8, 8, dtype=torch.float)

    torch.onnx.export(net, v_0, "tinycnn_pnnx_pnnx.py.onnx", export_params=True, operator_export_type=torch.onnx.OperatorExportTypes.ONNX_ATEN_FALLBACK, opset_version=13, input_names=['in0'], output_names=['out0'])

@torch.no_grad()
def test_inference():
    net = Model()
    net.float()
    net.eval()

    torch.manual_seed(0)
    v_0 = torch.rand(1, 1, 8, 8, dtype=torch.float)

    return net(v_0)

if __name__ == "__main__":
    print(test_inference())
