# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 14_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 135 bytes
import heapq

def vulnerable_function():
    heap = [1, 2, 3]
    heapq.heappushpop(heap, 4)
    return heap

# okay decompiling 14_1.pyc
