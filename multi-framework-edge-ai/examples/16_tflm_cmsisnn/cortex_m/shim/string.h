/* Freestanding builds have no libc headers. CMSIS-NN only needs these, implemented in startup.c. */
#pragma once
#include <stddef.h>
void* memcpy(void* d, const void* s, size_t n);
void* memset(void* d, int v, size_t n);
void* memmove(void* d, const void* s, size_t n);
