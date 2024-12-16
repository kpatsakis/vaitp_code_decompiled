# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1187_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 708 bytes


class RDMAOperation:

    def __init__(self, lkey):
        self.lkey = lkey

    def perform_atomic_operation(self):
        self.atomic_write()

    def atomic_write(self):
        if self.lkey != 1001:
            print("Performing atomic write with invalid lkey, potential kernel panic!")
        else:
            print("Atomic write operation successful.")


operation = RDMAOperation(lkey=9999)
operation.perform_atomic_operation()

# okay decompiling 1187_1.pyc
