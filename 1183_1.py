# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1183_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 520 bytes
import os

def read_dispatch_trace_log():
    try:
        with open("/sys/kernel/debug/powerpc/dtl/cpu-0", "r") as file:
            data = file.read()
            print(data)
    except Exception as e:
        try:
            print(f"Error reading dispatch trace log: {e}")
        finally:
            e = None
            del e


def main():
    read_dispatch_trace_log()


if __name__ == "__main__":
    main()

# okay decompiling 1183_1.pyc
