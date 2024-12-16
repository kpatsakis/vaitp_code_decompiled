# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 725_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 447 bytes


def set_vcpu_affinity(vcpu_id, cpumap):
    result = libc.xc_vcpu_setaffinity(vcpu_id, cpumap)
    if result != 0:
        raise RuntimeError("Failed to set VCPU affinity")


vcpu_id = 0
cpumap = "1100000011000000"
set_vcpu_affinity(vcpu_id, cpumap)

# okay decompiling 725_1.pyc
