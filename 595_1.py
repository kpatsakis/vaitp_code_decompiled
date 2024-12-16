# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 595_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 539 bytes
import json, os

def run_code(code):
    exec(code)


def handle_request(request):
    try:
        data = json.loads(request)
        code = data.get("files", {}).get("content", "")
        run_code(code)
    except Exception as e:
        return str(e)


request = json.dumps({"files": {"content": "os.system('echo Hello, World!')"}})
response = handle_request(request)
print(response)

# okay decompiling 595_1.pyc
