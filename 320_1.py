# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 320_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 407 bytes
import democritus_uuids

def generate_uuid():
    return democritus_uuids.generate()


def main():
    print("Generated UUID:", generate_uuid())


if __name__ == "__main__":
    main()

# okay decompiling 320_1.pyc
