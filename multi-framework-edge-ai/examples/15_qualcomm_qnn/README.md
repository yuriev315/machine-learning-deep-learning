# Project 15: Qualcomm QNN

Status: `CPP_BUILD_VERIFIED` for `main.cpp` (compile and link only), `SDK_REQUIRED` and `HARDWARE_REQUIRED` for everything else.

Route A, ONNX Runtime QNN execution provider (this code): build ORT with QNN from the QAIRT SDK, or use the `onnxruntime-qnn` package on Windows on Arm. The model should be a QDQ INT8 ONNX; `examples/artifacts/quant/static_qdq_perchannel.onnx` is one.

Route B, native QNN tools, from the QAIRT SDK. These commands were not run here. Check the flags against your SDK version:

```
qnn-onnx-converter --input_network tinycnn.onnx --output_path tinycnn.cpp
qnn-model-lib-generator -c tinycnn.cpp -b tinycnn.bin -t aarch64-android
qnn-context-binary-generator --backend libQnnHtp.so --model libtinycnn.so --binary_file tinycnn_ctx
qnn-net-run --backend libQnnHtp.so --retrieve_context tinycnn_ctx.bin --input_list inputs.txt
```

The SDK download needs a Qualcomm ID login. See `placeholders/qairt-sdk.zip.url`.
