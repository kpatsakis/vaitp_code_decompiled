# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 763_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 358 bytes
import jsonpickle

def vulnerable_deserialize(data):
    return jsonpickle.decode(data)


malicious_payload = '{"py/object": "__main__.YourMaliciousClass"}'
result = vulnerable_deserialize(malicious_payload)

# okay decompiling 763_1.pyc
