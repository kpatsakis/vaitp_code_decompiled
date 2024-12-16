# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1006_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 678 bytes


class VulnerableDynamicArray:

    def __init__(self):
        self.data = []

    def append(self, value):
        self.data.append(value)

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data[index] = value


array = VulnerableDynamicArray()
array.append(1)
array.append(2)
array.set(2, 3)
print(array.get(2))

# okay decompiling 1006_1.pyc
