# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 20_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 912 bytes
import ctypes
libkeccak = ctypes.CDLL("./libkeccak.so")
libkeccak.KeccakF_1600_32_rvk64.restype = None
libkeccak.KeccakF_1600_32_rvk64.argtypes = [ctypes.POINTER(ctypes.c_uint64), ctypes.POINTER(ctypes.c_uint64), ctypes.c_size_t]
state = (ctypes.c_uint64 * 25)()
input_data = (ctypes.c_uint64 * 1000)()
for i in range(1000):
    input_data[i] = i
else:
    libkeccak.KeccakF_1600_32_rvk64(state, input_data, ctypes.c_size_t(18446744073709551615))

# okay decompiling 20_1.pyc
