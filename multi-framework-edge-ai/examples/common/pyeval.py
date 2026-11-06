"""Python-side evaluator with the same output format as digits.h."""
import json, os, resource, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def load():
    d = np.load(os.path.join(HERE, "..", "data", "digits.npz"))
    return d["x_train"], d["y_train"], d["x_test"], d["y_test"]
def evaluate(route, predict, x_test, y_test, model_path=None, size=None):
    """predict(single image, HxW float32) -> logits. Runs one image at a time."""
    lat, hit = [], 0
    for x, y in zip(x_test, y_test):
        t = time.perf_counter(); o = predict(x); lat.append((time.perf_counter() - t) * 1e6)
        hit += int(np.argmax(o) == y)
    lat.sort()
    r = dict(route=route, n=len(lat), accuracy=round(hit / len(lat), 4), latency_mean_us=round(sum(lat) / len(lat), 2),
             latency_p95_us=round(lat[int(len(lat) * .95)], 2), peak_rss_kb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             model_bytes=size if size is not None else (os.path.getsize(model_path) if model_path else 0))
    print("RESULT " + json.dumps(r, separators=(",", ":")))
    return r
