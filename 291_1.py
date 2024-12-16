# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 291_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 467 bytes
import democritus_hashes

def insecure_hash(data):
    """Generates a hash of the input data using the vulnerable package."""
    return democritus_hashes.hash(data)


if __name__ == "__main__":
    user_input = "sensitive data"
    print("Insecure hash:", insecure_hash(user_input))

# okay decompiling 291_1.pyc
