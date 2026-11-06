cmake_minimum_required(VERSION 3.19)
project(et_digits CXX)
set(CMAKE_CXX_STANDARD 17)
set(ET_ROOT "" CACHE PATH "ExecuTorch install prefix")
set(ET_SRC_PARENT "" CACHE PATH "Directory containing the executorch source tree (extension headers are not installed by v0.6.0)")
set(L ${ET_ROOT}/lib)
add_executable(et_digits main.cpp)
target_compile_definitions(et_digits PRIVATE C10_USING_CUSTOM_GENERATED_MACROS)
target_include_directories(et_digits PRIVATE ${ET_ROOT}/include ${ET_SRC_PARENT} ${ET_SRC_PARENT}/executorch/runtime/core/portable_type/c10 ${CMAKE_CURRENT_SOURCE_DIR}/../common/cpp)
# Backends and kernels self-register in static initializers, so they must be linked whole or the linker drops them.
target_link_libraries(et_digits PRIVATE
  ${L}/libextension_module_static.a ${L}/libextension_data_loader.a ${L}/libextension_flat_tensor.a ${L}/libextension_tensor.a
  -Wl,--whole-archive ${L}/libxnnpack_backend.a ${L}/libportable_ops_lib.a -Wl,--no-whole-archive
  ${L}/libportable_kernels.a ${L}/libXNNPACK.a ${L}/libmicrokernels-prod.a ${L}/libextension_threadpool.a ${L}/libpthreadpool.a ${L}/libcpuinfo.a
  ${L}/libexecutorch.a ${L}/libexecutorch_core.a dl)
if(NOT ANDROID)
  target_link_libraries(et_digits PRIVATE pthread)
endif()
if(ANDROID)
  target_link_libraries(et_digits PRIVATE log)
endif()
