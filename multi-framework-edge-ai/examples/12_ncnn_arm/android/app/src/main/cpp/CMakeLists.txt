cmake_minimum_required(VERSION 3.18)
project(ncnndigits)
# Point ncnn_DIR at the unpacked ncnn-20250503-android archive: <sdk>/${ANDROID_ABI}/lib/cmake/ncnn
find_package(ncnn REQUIRED)
add_library(ncnndigits SHARED jni_digits.cpp)
target_link_libraries(ncnndigits ncnn android log)
