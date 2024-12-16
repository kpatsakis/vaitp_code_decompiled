# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1116_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 488 bytes
import eventlet

def vulnerable_eventlet_function():

    def worker():
        print("Worker function is running")

    eventlet.spawn(worker)
    eventlet.sleep(1)


vulnerable_eventlet_function()

# okay decompiling 1116_1.pyc
