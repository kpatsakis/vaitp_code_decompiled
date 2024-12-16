# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 205_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 335 bytes
import zlib

def decompress(data):
    d = zlib.decompressobj()
    return d.decompress(data)


malicious_input = b'x\xda\xbc\x02\xff\xff\xff\xff'
try:
    decompress(malicious_input)
except Exception as e:
    try:
        print(f"Error: {e}")
    finally:
        e = None
        del e

# okay decompiling 205_1.pyc
