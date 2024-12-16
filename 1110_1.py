# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1110_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 639 bytes
from fastecdsa import curve, ecdsa

def unsafe_curvemath_mul(point, scalar):
    return point * scalar


G = curve.P256.G
k = None
result = unsafe_curvemath_mul(G, k)
print("Result:", result)

# okay decompiling 1110_1.pyc
