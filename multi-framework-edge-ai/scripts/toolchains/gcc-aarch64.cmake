# Local GCC 15 cross toolchain (unpacked Ubuntu debs, no system install). Needs glibc >= the unpacked sysroot's 2.43 on the target;
# use zig-aarch64.cmake when the binary must also run on devices with older glibc.
set(CMAKE_SYSTEM_NAME Linux)
set(CMAKE_SYSTEM_PROCESSOR aarch64)
set(CMAKE_C_COMPILER $ENV{MFEA_ROOT}/.envs/tools/bin/a64-gcc)
set(CMAKE_CXX_COMPILER $ENV{MFEA_ROOT}/.envs/tools/bin/a64-g++)
set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
