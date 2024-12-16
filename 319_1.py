# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 319_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 347 bytes
import requests

def insecure_uuid_generation():
    response = requests.get("http://malicious-url.com/get-uuid")
    return response.text


if __name__ == "__main__":
    print("Generated UUID:", insecure_uuid_generation())

# okay decompiling 319_1.pyc
