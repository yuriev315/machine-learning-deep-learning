# source me: shared environment for the project.
export MFEA_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPYCACHEPREFIX="$MFEA_ROOT/.envs/pycache"   # never write bytecode next to shared/reused packages
export OMP_NUM_THREADS=${OMP_NUM_THREADS:-4} OPENBLAS_NUM_THREADS=4 MKL_NUM_THREADS=4 XLA_FLAGS="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=4"
export JAX_PLATFORMS=cpu KERAS_BACKEND=jax CUDA_VISIBLE_DEVICES=""
export PATH="$MFEA_ROOT/.envs/main/bin:$MFEA_ROOT/.envs/tools/bin:$HOME/.local/bin:$PATH"
export A64_SYSROOT="$MFEA_ROOT/third_party/gcc-aarch64/usr/aarch64-linux-gnu"
