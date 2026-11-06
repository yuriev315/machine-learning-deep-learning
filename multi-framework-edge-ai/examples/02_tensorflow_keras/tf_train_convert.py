#!/usr/bin/env python3
"""Project 02: TensorFlow 2.19 + Keras 3 training -> .keras, .h5, SavedModel, frozen GraphDef -> .tflite FP32, dynamic range, full INT8 -> ONNX via tf2onnx."""
import json, os, sys, warnings
warnings.simplefilter("ignore"); os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"; os.environ["KERAS_BACKEND"] = "tensorflow"
import numpy as np, tensorflow as tf, keras
H = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(H, "..", "artifacts", "tensorflow"); os.makedirs(OUT, exist_ok=True)
d = np.load(os.path.join(H, "..", "data", "digits.npz"))
xtr, ytr, xte, yte = d["x_train"][..., None], d["y_train"], d["x_test"][..., None], d["y_test"]
keras.utils.set_random_seed(20250601)
L = keras.layers
m = keras.Sequential([keras.Input((8, 8, 1), batch_size=None), L.Conv2D(8, 3, padding="same", activation="relu"), L.MaxPool2D(2), L.Conv2D(16, 3, padding="same", activation="relu"), L.MaxPool2D(2), L.Flatten(), L.Dense(10)])
m.compile(keras.optimizers.Adam(3e-3), keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
m.fit(xtr, ytr, batch_size=64, epochs=40, verbose=0)
print("keras test accuracy", m.evaluate(xte, yte, verbose=0)[1])
m.save(os.path.join(OUT, "tinycnn.keras")); m.save(os.path.join(OUT, "tinycnn.h5"))
sm = os.path.join(OUT, "saved_model"); m.export(sm, format="tf_saved_model", verbose=False)
fn = tf.function(lambda x: m(x, training=False), input_signature=[tf.TensorSpec([1, 8, 8, 1], tf.float32, name="input")])
cf = fn.get_concrete_function()
from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
frozen = convert_variables_to_constants_v2(cf); tf.io.write_graph(frozen.graph.as_graph_def(), OUT, "tinycnn_frozen.pb", as_text=False)
print("graphdef inputs", [t.name for t in frozen.inputs], "outputs", [t.name for t in frozen.outputs])
def conv():
    return tf.lite.TFLiteConverter.from_concrete_functions([cf], fn)
open(os.path.join(OUT, "tinycnn_float.tflite"), "wb").write(conv().convert())
c = conv(); c.optimizations = [tf.lite.Optimize.DEFAULT]
open(os.path.join(OUT, "tinycnn_dynrange.tflite"), "wb").write(c.convert())
def rep():
    for x in xtr[:200]:
        yield [x[None].astype(np.float32)]
c = conv(); c.optimizations = [tf.lite.Optimize.DEFAULT]; c.representative_dataset = rep
c.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]; c.inference_input_type = tf.int8; c.inference_output_type = tf.int8
open(os.path.join(OUT, "tinycnn_int8.tflite"), "wb").write(c.convert())
try:
    import tf2onnx
    tf2onnx.convert.from_function(fn, input_signature=fn.input_signature, opset=17, output_path=os.path.join(OUT, "tinycnn_tf2onnx.onnx"))
    print("tf2onnx ok")
except Exception as e:
    print("tf2onnx failed:", type(e).__name__, str(e)[:200])
print("sizes", {n: os.path.getsize(os.path.join(OUT, n)) for n in sorted(os.listdir(OUT)) if os.path.isfile(os.path.join(OUT, n))})
