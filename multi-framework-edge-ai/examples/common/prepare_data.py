#!/usr/bin/env python3
"""Shared real dataset: UCI optical digits via scikit-learn (1797 8x8 grayscale images, BSD-licensed).
Every route in this project is evaluated on this same fixed test split, so the numbers are comparable.
Writes digits.npz and digits_test.bin (uint32 n,h,w; n*h*w float32; n uint8 labels)."""
import os, struct, numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data"); os.makedirs(out, exist_ok=True)
d = load_digits()
x = (d.images.astype(np.float32) / 16.0 - 0.5) / 0.5   # scale to [-1, 1]
y = d.target.astype(np.int64)
xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.25, random_state=20250601, stratify=y)
np.savez_compressed(os.path.join(out, "digits.npz"), x_train=xtr, y_train=ytr, x_test=xte, y_test=yte)
with open(os.path.join(out, "digits_test.bin"), "wb") as f:
    f.write(struct.pack("<III", len(xte), 8, 8)); f.write(xte.astype("<f4").tobytes()); f.write(yte.astype(np.uint8).tobytes())
print("train", xtr.shape, "test", xte.shape)
