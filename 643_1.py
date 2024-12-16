# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 643_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 630 bytes
import pickle

def load_data(serialized_data):
    return pickle.loads(serialized_data)


def handle_request(serialized_data):
    try:
        data = load_data(serialized_data)
        print("Data processed:", data)
    except Exception as e:
        try:
            print("Error processing data:", e)
        finally:
            e = None
            del e


crafted_data = b'\x80\x03}q\x00X\x03\x00\x00\x00keyq\x01X\x05\x00\x00\x00valueq\x02.'
handle_request(crafted_data)

# okay decompiling 643_1.pyc
