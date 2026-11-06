#!/usr/bin/env python3
"""Project 03: Flax training -> Orbax checkpoint -> jax.export StableHLO -> IREE VMFB -> IREE runtime.
Project 02b: Keras 3 (JAX backend) training -> .keras -> StableHLO -> same IREE path."""
import os, subprocess, sys
import jax, jax.numpy as jnp, numpy as np, optax, flax.linen as nn, orbax.checkpoint as ocp
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "common"))
from pyeval import load, evaluate
A = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts"))
OUT = os.path.join(A, "jax"); KOUT = os.path.join(A, "keras"); os.makedirs(OUT, exist_ok=True); os.makedirs(KOUT, exist_ok=True)
xtr, ytr, xte, yte = load(); xtr, xte = xtr[..., None], xte[..., None]
class TinyCNN(nn.Module):
    @nn.compact
    def __call__(s, x):
        x = nn.max_pool(nn.relu(nn.Conv(8, (3, 3))(x)), (2, 2), (2, 2))
        x = nn.max_pool(nn.relu(nn.Conv(16, (3, 3))(x)), (2, 2), (2, 2))
        return nn.Dense(10)(x.reshape((x.shape[0], -1)))
m = TinyCNN(); key = jax.random.PRNGKey(20250601); params = m.init(key, jnp.zeros((1, 8, 8, 1)))
tx = optax.adam(3e-3); st = tx.init(params)
@jax.jit
def step(p, s, x, y):
    l, g = jax.value_and_grad(lambda p: optax.softmax_cross_entropy_with_integer_labels(m.apply(p, x), y).mean())(p)
    u, s = tx.update(g, s); return optax.apply_updates(p, u), s, l
rng = np.random.default_rng(20250601)
for ep in range(40):
    idx = rng.permutation(len(xtr))
    for i in range(0, len(idx), 64):
        b = idx[i:i + 64]
        if len(b) == 64:
            params, st, _ = step(params, st, xtr[b], ytr[b])
ckdir = os.path.join(OUT, "orbax_ckpt")
with ocp.StandardCheckpointer() as ck:
    if os.path.exists(ckdir):
        import shutil; shutil.rmtree(ckdir)
    ck.save(ckdir, params)
with ocp.StandardCheckpointer() as ck:
    params = ck.restore(ckdir, params)
from jax import export as jx
def to_vmfb(fn, shape, stem):
    e = jx.export(jax.jit(fn))(jax.ShapeDtypeStruct(shape, jnp.float32))
    mlir = stem + ".stablehlo.mlir"; open(mlir, "w").write(e.mlir_module()); open(stem + ".jaxexport", "wb").write(e.serialize())
    vm = stem + ".vmfb"
    subprocess.check_call(["iree-compile", "--iree-input-type=stablehlo", "--iree-hal-target-backends=llvm-cpu", "--iree-llvmcpu-target-cpu=x86-64-v3", mlir, "-o", vm])
    return vm
def iree_session(vm):
    import iree.runtime as rt
    cfg = rt.Config("local-sync"); ctx = rt.SystemContext(config=cfg)
    vm_mod = rt.VmModule.mmap(ctx.instance, vm); ctx.add_vm_module(vm_mod); return ctx.modules[vm_mod.name]["main"]
apply = lambda x: m.apply(params, x)
evaluate("flax_jit_py", (lambda f: lambda x: np.asarray(f(x[None, ..., None] if x.ndim == 2 else x[None])[0]))(jax.jit(apply)), xte, yte, size=int(sum(np.asarray(v).nbytes for v in jax.tree_util.tree_leaves(params))))
vm = to_vmfb(apply, (1, 8, 8, 1), os.path.join(OUT, "tinycnn"))
f = iree_session(vm)
evaluate("jax_stablehlo_iree_py", lambda x: np.asarray(f(x[None]))[0], xte, yte, vm)
# ---- Keras 3 on JAX backend ----
os.environ["KERAS_BACKEND"] = "jax"
import keras
keras.utils.set_random_seed(20250601)
L = keras.layers
km = keras.Sequential([keras.Input((8, 8, 1)), L.Conv2D(8, 3, padding="same", activation="relu"), L.MaxPool2D(2), L.Conv2D(16, 3, padding="same", activation="relu"), L.MaxPool2D(2), L.Flatten(), L.Dense(10)])
km.compile(keras.optimizers.Adam(3e-3), keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=["accuracy"])
km.fit(xtr, ytr, batch_size=64, epochs=40, verbose=0)
print("keras3 test accuracy", km.evaluate(xte, yte, verbose=0)[1])
kp = os.path.join(KOUT, "tinycnn.keras"); km.save(kp); km.save(os.path.join(KOUT, "tinycnn.h5"))
km2 = keras.models.load_model(kp)
tv, ntv = km2.trainable_variables, km2.non_trainable_variables
tv = [v.value for v in tv]; ntv = [v.value for v in ntv]
kapply = lambda x: km2.stateless_call(tv, ntv, x, training=False)[0]
kv = to_vmfb(kapply, (1, 8, 8, 1), os.path.join(KOUT, "tinycnn"))
kf = iree_session(kv)
evaluate("keras3_jax_stablehlo_iree_py", lambda x: np.asarray(kf(x[None]))[0], xte, yte, kv)
try:
    km2.export(os.path.join(KOUT, "savedmodel"), format="tf_saved_model")
    print("keras tf_saved_model export: OK")
except Exception as e:
    print("keras tf_saved_model export: UNSUPPORTED here,", type(e).__name__, str(e)[:120])
