#!/usr/bin/env bash
# Project 20: package a runtime with its exact library closure, then run it in an isolated root that has nothing else.
# The chroot has an empty environment and no network. It stands in for a clean device, but it is not one:
# the kernel and CPU are still this host, so the result is never recorded as DEVICE_DEPLOYMENT_VERIFIED.
cd "$(dirname "$0")/../.." && source scripts/env.sh
O=$PWD/build/package; rm -rf $O; P=$O/digits-ort-linux-x64-1.0; mkdir -p $P/bin $P/lib $P/model
cmake --install build/x64/ort --prefix $P >/dev/null   # install step swaps the build RPATH for $ORIGIN/../lib, removing absolute host paths
cp -L third_party/onnxruntime-x64/lib/libonnxruntime.so.1.22.0 $P/lib/ 2>/dev/null || cp -L third_party/onnxruntime-x64/lib/libonnxruntime.so* $P/lib/
SONAME=$(readelf -d $P/bin/ort_digits | sed -n 's/.*NEEDED.*\[\(libonnxruntime[^]]*\)\].*/\1/p'); [ -f $P/lib/$SONAME ] || ln -sf $(ls $P/lib | head -1) $P/lib/$SONAME
cp examples/artifacts/pytorch/tinycnn.onnx examples/data/digits_test.bin $P/model/
cat > $P/run.sh <<'S'
#!/bin/sh
# LD_LIBRARY_PATH as well as RUNPATH: glibc resolves $ORIGIN through /proc, which minimal roots may not have mounted
d="${0%/*}"; LD_LIBRARY_PATH="$d/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"; export LD_LIBRARY_PATH; exec "$d/bin/ort_digits" "$d/model/tinycnn.onnx" "$d/model/digits_test.bin" "${1:-1}" packaged_ort_cpp
S
chmod +x $P/run.sh
readelf -d $P/bin/ort_digits | grep -E 'RPATH|RUNPATH' | cut -c1-120
(cd $O && tar czf digits-ort-linux-x64-1.0.tar.gz digits-ort-linux-x64-1.0); ls -la $O/*.tar.gz | awk '{print "package_bytes",$5}'
R=$O/clean_root; mkdir -p $R/app; tar xzf $O/digits-ort-linux-x64-1.0.tar.gz -C $R/app --strip-components=1
for f in $(ldd $P/bin/ort_digits $P/lib/libonnxruntime.so* | awk '/=> \//{print $3} /^\s*\/lib/{print $1}' | grep -v "^$O" | sort -u); do mkdir -p $R$(dirname $f); cp -L $f $R$f; done
mkdir -p $R/lib64; cp -L /lib64/ld-linux-x86-64.so.2 $R/lib64/; mkdir -p $R/bin; cp /bin/dash $R/bin/sh; for f in $(ldd /bin/dash | awk '/=> \//{print $3}'); do mkdir -p $R$(dirname $f); cp -L $f $R$f; done
echo "clean root files: $(find $R -type f | wc -l), size: $(du -sh $R | cut -f1)"; find $R -type f -not -path '*/app/*' | sed "s|$R||" | sort | tr '\n' ' '; echo
env -i unshare --net chroot $R /app/run.sh 1
