# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1069_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 558 bytes
import json, os
from processing_utils import move_files_to_cache

def postprocess(user_input):
    parsed_json = json.loads(user_input)
    if isinstance(parsed_json, dict):
        if "path" in parsed_json:
            file_path = parsed_json["path"]
            move_files_to_cache(file_path)


user_input = '{"path": "/etc/passwd"}'
postprocess(user_input)

# okay decompiling 1069_1.pyc
