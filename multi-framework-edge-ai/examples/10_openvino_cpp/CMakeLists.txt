cmake_minimum_required(VERSION 3.16)
project(ov_digits CXX)
set(CMAKE_CXX_STANDARD 17)
find_package(OpenVINO REQUIRED COMPONENTS Runtime)   # -DOpenVINO_DIR=<sdk>/runtime/cmake
add_executable(ov_digits main.cpp)
target_include_directories(ov_digits PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/../common/cpp)
target_link_libraries(ov_digits PRIVATE openvino::runtime)
