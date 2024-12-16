# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 377_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 475 bytes
import json

def process_request(request):
    data = json.loads(request.get("data"))
    if "command" in data:
        exec(data["command"])


malicious_request = {"data": '{"command": "__import__(\'os\').system(\'cat  /etc/passwd\')"}'}
process_request(malicious_request)

# okay decompiling 377_1.pyc
