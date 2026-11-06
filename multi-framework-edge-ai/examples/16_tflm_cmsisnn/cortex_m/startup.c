/* Minimal Cortex-M vector table and C runtime: copy .data, clear .bss, run main, exit through semihosting. */
#include <stddef.h>
#include <stdint.h>
extern uint32_t _sidata, _sdata, _edata, _sbss, _ebss, _estack;
int main(void);
#ifndef USE_LIBC
/* Word-at-a-time when aligned. */
void* memcpy(void* d, const void* s, size_t n) {
  uint8_t* a = d; const uint8_t* b = s;
  if ((((uintptr_t)a | (uintptr_t)b) & 3) == 0) { for (; n >= 4; n -= 4, a += 4, b += 4) *(uint32_t*)a = *(const uint32_t*)b; }
  while (n--) *a++ = *b++;
  return d;
}
void* memset(void* d, int v, size_t n) {
  uint8_t* a = d; uint32_t w = (uint8_t)v * 0x01010101u;
  while (n && ((uintptr_t)a & 3)) { *a++ = (uint8_t)v; --n; }
  for (; n >= 4; n -= 4, a += 4) *(uint32_t*)a = w;
  while (n--) *a++ = (uint8_t)v;
  return d;
}
void* memmove(void* d, const void* s, size_t n) { uint8_t* a = d; const uint8_t* b = s; if (a < b) { while (n--) *a++ = *b++; } else { a += n; b += n; while (n--) *--a = *--b; } return d; }
void __aeabi_memcpy(void* d, const void* s, size_t n) { memcpy(d, s, n); }
void __aeabi_memset(void* d, size_t n, int v) { memset(d, v, n); }
void __aeabi_memclr(void* d, size_t n) { memset(d, 0, n); }
void __aeabi_memcpy4(void* d, const void* s, size_t n) { memcpy(d, s, n); }
void __aeabi_memclr4(void* d, size_t n) { memset(d, 0, n); }
void __aeabi_memset4(void* d, size_t n, int v) { memset(d, v, n); }
void __aeabi_memmove(void* d, const void* s, size_t n) { memmove(d, s, n); }
#endif
static void semihost_exit(uint32_t ok) {
  static uint32_t block[2]; block[0] = ok ? 0x20026u : 0x20024u; block[1] = 0;
  register uint32_t r0 __asm("r0") = 0x20; register void* r1 __asm("r1") = block;
  __asm volatile("bkpt 0xAB" : : "r"(r0), "r"(r1) : "memory");
}
#ifdef USE_LIBC
void _init(void) {}
void _fini(void) {}
#endif
void Reset_Handler(void) {
#if defined(__ARM_FEATURE_MVE)
  *(volatile uint32_t*)0xE000ED88 |= (0xFu << 20);  /* CPACR: enable MVE/FP coprocessors */
  __asm volatile("dsb\n isb");
#endif
  uint32_t* s = &_sidata; uint32_t* d = &_sdata; while (d < &_edata) *d++ = *s++;
  for (d = &_sbss; d < &_ebss;) *d++ = 0;
#ifdef USE_LIBC
  extern void __libc_init_array(void); __libc_init_array();   /* C++ static constructors */
#endif
  semihost_exit(main() == 0);
  for (;;) {}
}
static void fault(void) { for (;;) {} }
__attribute__((section(".isr_vector"), used)) const void* vectors[16] = {&_estack, Reset_Handler, fault, fault, fault, fault, fault};
