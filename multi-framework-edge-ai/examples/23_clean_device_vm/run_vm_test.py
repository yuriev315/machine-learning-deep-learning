#!/usr/bin/env python3
"""Project 23: deploy to a clean, fully emulated ARM64 computer and measure accuracy there.

Boots an unmodified Debian 12 arm64 cloud image in qemu-system-aarch64 (virt, Cortex-A76, TCG), logs in over the serial console, reads the
package from a second virtual disk (this QEMU build has no network backend), unpacks it and runs it. The guest has its own kernel, libc and filesystem, and shares nothing
with the host, so this is much closer to a device than a chroot. It is still an emulator: timing is meaningless, and no board or peripheral is involved.
"""
import os, re, select, shutil, subprocess, time
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
QB = os.path.join(R, "third_party/qemu-arm/bin"); IMG = os.path.join(R, "deps/archives/debian-12-arm64/debian-12-nocloud-arm64.qcow2"); PKG_DIR = os.path.join(R, "build/vm_pkg")
FW = next(p for p in [os.path.join(R, "third_party/qemu-arm/share/qemu/edk2-aarch64-code.fd"), os.path.join(R, "third_party/qemu-arm/share/qemu/QEMU_EFI.fd")] if os.path.exists(p))
TIMEOUT = int(os.environ.get("VM_TIMEOUT", "1500"))
def main():
    work = os.path.join(R, "build/vm"); os.makedirs(work, exist_ok=True)
    disk = os.path.join(work, "disk.qcow2"); shutil.copy(IMG, disk)    # always start from the pristine image
    code = os.path.join(work, "code.fd"); vars_ = os.path.join(work, "vars.fd")
    b = open(FW, "rb").read(); s = 64 * 1024 * 1024; open(code, "wb").write(b + b"\0" * (s - len(b))); open(vars_, "wb").write(b"\0" * s)
    tarf = os.path.join(work, "pkg_disk.tar"); subprocess.check_call(["tar", "cf", tarf, "-C", PKG_DIR, "pkg"])
    pad = (-os.path.getsize(tarf)) % (1024 * 1024)
    with open(tarf, "ab") as f: f.write(b"\0" * pad)   # block devices need whole sectors; tar ignores trailing zeros
    cmd = [os.path.join(QB, "qemu-system-aarch64"), "-M", "virt", "-cpu", "cortex-a76", "-smp", "2", "-m", "1536", "-nographic", "-no-reboot",
           "-drive", f"if=pflash,format=raw,readonly=on,file={code}", "-drive", f"if=pflash,format=raw,file={vars_}",
           "-drive", f"if=virtio,format=qcow2,file={disk}", "-drive", f"if=virtio,format=raw,readonly=on,file={tarf}"]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0)
    buf = bytearray(); t0 = time.time(); log = open(os.path.join(R, "logs/step_vm_console.log"), "wb")
    def wait(pat, timeout):
        end = time.time() + timeout
        while time.time() < end and time.time() - t0 < TIMEOUT:
            if select.select([p.stdout], [], [], 2)[0]:
                d = os.read(p.stdout.fileno(), 65536)
                if not d: raise RuntimeError("VM exited")
                buf.extend(d); log.write(d); log.flush()
            m = re.search(pat, buf)
            if m:
                out = bytes(buf[:m.end()]); del buf[:m.end()]; return out
        raise TimeoutError(pat)
    def send(c): p.stdin.write(c.encode() + b"\n")
    try:
        wait(rb"login:", 1200); print(f"booted in {time.time() - t0:.0f}s", flush=True)
        send("root"); wait(rb"[#$] $", 120)
        send("uname -a; cat /etc/debian_version; nproc; grep -c . /proc/cpuinfo; ldd --version | head -1; echo READY\"\"1"); print(wait(rb"READY1\r?\n.*?[#$] ", 60).decode(errors="ignore")[-400:], flush=True)
        send("cd /root && tar xf /dev/vdb && cd pkg && ls && echo GOT\"\"_PKG"); wait(rb"GOT_PKG\r?\n", 300); print("package deployed from the second virtual disk", flush=True)
        # The quotes stop the serial echo of these commands from matching the end markers.
        send("sh run_all.sh 2>&1; echo ALL\"\"_DONE"); out = wait(rb"ALL_DONE\r?\n", 900).decode(errors="ignore")
        for line in out.splitlines():
            if line.startswith("RESULT "): print(line.strip(), flush=True)
            if line.startswith("LOG "): print(line.strip(), flush=True)
        send("poweroff")
        time.sleep(5)
    finally:
        p.kill()
main()
