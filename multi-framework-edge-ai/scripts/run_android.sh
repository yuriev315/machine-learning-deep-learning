#!/usr/bin/env bash
# Starts the emulator, runs the deployment test, and stops the emulator again even if the test fails.
cd "$(dirname "$0")/.." && source scripts/env.sh
ADB=third_party/android/platform-tools/adb; $ADB start-server >/dev/null 2>&1
timeout 1200 scripts/android_emulator.sh > logs/emulator.log 2>&1 &
EMU=$!
trap '$ADB -s emulator-5580 emu kill >/dev/null 2>&1; kill $EMU 2>/dev/null; wait $EMU 2>/dev/null' EXIT
examples/24_android_emulator/deploy_and_run.sh
