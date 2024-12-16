# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 383_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 641 bytes


class OutputFilter:

    def __init__(self):
        self.buffer = bytearray()

    def read(self, size):
        if size > 16384:
            data = self._read_from_source(size)
            self.buffer.extend(data)
            return data
        return self.buffer[None[:size]]

    def _read_from_source(self, size):
        return b'Some data' * (size // 10)

# okay decompiling 383_1.pyc
