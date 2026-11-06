/* QEMU mps2-an386 and mps3-an547: code RAM at 0, data RAM at 0x20000000. On a real board, set these from the datasheet. */
MEMORY { FLASH (rx) : ORIGIN = 0x00000000, LENGTH = 512K  RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 128K }
ENTRY(Reset_Handler)
SECTIONS {
  .isr_vector : { KEEP(*(.isr_vector)) } > FLASH
  .text : { *(.text*) *(.rodata*) . = ALIGN(4); } > FLASH
  .ARM.exidx : { *(.ARM.exidx*) } > FLASH
  _sidata = LOADADDR(.data);
  .data : { . = ALIGN(4); _sdata = .; *(.data*) . = ALIGN(4); _edata = .; } > RAM AT > FLASH
  .bss (NOLOAD) : { . = ALIGN(4); _sbss = .; *(.bss*) *(COMMON) . = ALIGN(4); _ebss = .; } > RAM
  _estack = ORIGIN(RAM) + LENGTH(RAM);
}
