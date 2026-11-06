cmake_minimum_required(VERSION 3.16)
project(paddle_lite_mobilenet CXX)
set(CMAKE_CXX_STANDARD 14)
set(PADDLE_LITE_CXX "" CACHE PATH "inference_lite_lib.*/cxx directory")
add_executable(paddle_mobilenet main.cpp)
target_include_directories(paddle_mobilenet PRIVATE ${PADDLE_LITE_CXX}/include)
target_compile_options(paddle_mobilenet PRIVATE -include cstdint)  # the 2.12 headers rely on an implicit cstdint that newer GCC no longer provides
target_link_libraries(paddle_mobilenet PRIVATE ${PADDLE_LITE_CXX}/lib/libpaddle_light_api_shared.so -fopenmp)  # the prebuilt library needs libgomp
set_target_properties(paddle_mobilenet PROPERTIES BUILD_RPATH "\$ORIGIN")
add_executable(paddle_digits digits_main.cpp)
target_include_directories(paddle_digits PRIVATE ${PADDLE_LITE_CXX}/include ${CMAKE_CURRENT_SOURCE_DIR}/../common/cpp)
target_compile_options(paddle_digits PRIVATE -include cstdint)
target_link_libraries(paddle_digits PRIVATE ${PADDLE_LITE_CXX}/lib/libpaddle_light_api_shared.so -fopenmp)
set_target_properties(paddle_digits PROPERTIES BUILD_RPATH "\$ORIGIN")
