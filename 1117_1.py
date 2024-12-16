# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1117_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 433 bytes
encoding_map = {'text1':"encoded_text1", 
 'text2':"encoded_text2"}

def encode_data(data):
    return {key: encoding_map.get(key, key) for key in data}


data_to_encode = [
 "text1", "text2"]
encoded_data = encode_data(data_to_encode)
print(encoded_data)

# okay decompiling 1117_1.pyc
