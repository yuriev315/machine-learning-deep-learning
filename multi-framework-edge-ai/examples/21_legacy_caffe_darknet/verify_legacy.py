#!/usr/bin/env python3
"""Project 21: real legacy models. Caffe SqueezeNet 1.1 and Darknet YOLOv4-tiny, converted to ncnn, run on a real photo
(Darknet's data/dog.jpg). OpenCV DNN loads the ORIGINAL Caffe/Darknet files as an independent reference."""
import os, sys
import cv2, ncnn, numpy as np
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
A, T, DA = os.path.join(R, "examples/artifacts"), os.path.join(R, "third_party"), os.path.join(R, "deps/archives")
img = cv2.imread(os.path.join(T, "darknet/data/dog.jpg")); assert img is not None
names = open(os.path.join(T, "darknet/data/coco.names")).read().split("\n")
# --- Caffe ---
m = cv2.resize(img, (227, 227)).astype(np.float32) - np.array([104, 117, 123], np.float32)
ref = cv2.dnn.readNetFromCaffe(os.path.join(DA, "squeezenet11-prototxt/deploy.prototxt"), os.path.join(DA, "squeezenet11-caffemodel/squeezenet_v1.1.caffemodel"))
ref.setInput(m.transpose(2, 0, 1)[None]); r = ref.forward().flatten()
net = ncnn.Net(); net.load_param(os.path.join(A, "caffe/squeezenet.param")); net.load_model(os.path.join(A, "caffe/squeezenet.bin"))
chw = m.transpose(2, 0, 1).copy()   # keep a reference: ncnn.Mat wraps this memory without copying
ex = net.create_extractor(); ex.input("data", ncnn.Mat(chw))
_, o = ex.extract("prob"); o = np.array(o).flatten()
print(f"caffe: opencv top5 {r.argsort()[-5:][::-1].tolist()}  ncnn top5 {o.argsort()[-5:][::-1].tolist()}  max|diff| {np.abs(r - o).max():.5f}", flush=True)
# --- Darknet ---
rgb = cv2.cvtColor(cv2.resize(img, (416, 416)), cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
d = ncnn.Net(); d.load_param(os.path.join(A, "darknet/yolov4tiny.param")); d.load_model(os.path.join(A, "darknet/yolov4tiny.bin"))
chw2 = rgb.transpose(2, 0, 1).copy()
ex = d.create_extractor(); ex.input("data", ncnn.Mat(chw2))
rc, om = ex.extract("output")
print("ncnn extract rc", rc, "rows", om.h, "cols", om.w, flush=True)
if om.w > 0:
    out = np.array(om)
    if out.ndim == 1: out = out[None]
    print("darknet via ncnn: detections", [(names[int(c) - 1], round(float(s), 3)) for c, s, *_ in out[np.argsort(-out[:, 1])]][:6], flush=True)
D = cv2.dnn.readNetFromDarknet(os.path.join(DA, "yolov4-tiny-cfg/yolov4-tiny.cfg"), os.path.join(DA, "yolov4-tiny-weights/yolov4-tiny.weights"))
D.setInput(cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False))
det = np.vstack(D.forward(D.getUnconnectedOutLayersNames())); det = det[det[:, 4] > 0.25]
idx = cv2.dnn.NMSBoxes(det[:, :4].tolist(), (det[:, 5:].max(1)).tolist(), 0.25, 0.45)
print("darknet via opencv reference:", sorted({names[int(det[i, 5:].argmax())] for i in np.array(idx).flatten()}))
