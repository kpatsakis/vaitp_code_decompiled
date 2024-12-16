# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 986_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 449 bytes


def resolve_axis(axis, tensor_shape):
    if axis < 0:
        axis += len(tensor_shape)
    return axis


tensor_shape = [
 3, 4, 5]
axis = -1
resolved_axis = resolve_axis(axis, tensor_shape)
print(f"Resolved axis: {resolved_axis}")
print(f"Accessing tensor at resolved axis: {tensor_shape[resolved_axis]}")

# okay decompiling 986_1.pyc
