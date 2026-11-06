#!/usr/bin/env bash
# Run a command under strict resource limits: this host also runs live services.
# Cgroup scope: at most 4 CPUs, 12 GiB RAM, low CPU/IO weight. Limits vanish when the command exits.
exec systemd-run --scope --quiet --collect \
  -p CPUQuota=${LOWPRIO_CPU:-400}% -p CPUWeight=20 -p IOWeight=20 -p MemoryMax=${LOWPRIO_MEM:-12G} -p MemorySwapMax=0 \
  nice -n 15 "$@"
