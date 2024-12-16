# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 256_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 763 bytes


class TlsLite:

    def __init__(self):
        self.buffer = bytearray(10)

    def receive_data(self, data):
        for i in range(len(data)):
            self.buffer[i] = data[i]

    def process_data(self):
        print("Processing data:", self.buffer)


tls_lite = TlsLite()
malicious_data = bytearray(100)
try:
    tls_lite.receive_data(malicious_data)
    tls_lite.process_data()
except IndexError as e:
    try:
        print("Caught an exception:", e)
    finally:
        e = None
        del e

# okay decompiling 256_1.pyc
