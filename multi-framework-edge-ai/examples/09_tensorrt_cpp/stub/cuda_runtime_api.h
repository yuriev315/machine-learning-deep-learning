/* Minimal stand-in for CUDA's header, used ONLY to syntax-check main.cpp against the official TensorRT headers on a machine with no CUDA.
 * Do not ship with this. A real build uses the CUDA toolkit's own header. */
#pragma once
#include <stddef.h>
typedef struct CUstream_st* cudaStream_t;
typedef struct CUevent_st* cudaEvent_t;
typedef int cudaError_t;
