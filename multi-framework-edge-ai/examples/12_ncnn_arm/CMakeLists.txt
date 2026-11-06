cmake_minimum_required(VERSION 3.16)
project(ncnn_digits CXX)
set(CMAKE_CXX_STANDARD 17)
find_package(OpenMP)
find_package(ncnn REQUIRED)    # -Dncnn_DIR=<sdk>/lib/cmake/ncnn
add_executable(ncnn_digits main.cpp)
target_include_directories(ncnn_digits PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../common/cpp)
target_link_libraries(ncnn_digits PRIVATE ncnn)
# The Android build of ncnn exports -fno-exceptions and -fno-rtti; this program reports errors with exceptions.
set_property(SOURCE main.cpp PROPERTY COMPILE_OPTIONS -fexceptions -frtti)  # source options come after the exported target options
