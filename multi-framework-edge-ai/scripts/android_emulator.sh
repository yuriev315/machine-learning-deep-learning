#!/usr/bin/env bash
# Starts a headless Android 14 x86_64 emulator with KVM. The AVD lives in the project and its data is wiped on each start.
cd "$(dirname "$0")/.."
export ANDROID_SDK_ROOT=$PWD/third_party/android ANDROID_HOME=$PWD/third_party/android ANDROID_AVD_HOME=$PWD/.android_avd ANDROID_EMULATOR_HOME=$PWD/.android_avd/home
mkdir -p "$ANDROID_EMULATOR_HOME"
# The emulator segfaults when libX11-xcb is missing, even with -no-window. Servers have no X11, so point it at unpacked copies.
export LD_LIBRARY_PATH=$PWD/third_party/local_x11:$LD_LIBRARY_PATH
exec third_party/android/emulator/emulator -avd mfea -no-window -no-audio -no-boot-anim -no-snapshot -wipe-data -accel on -gpu swiftshader_indirect -memory 2048 -cores 2 -no-metrics -ports 5580,5581
