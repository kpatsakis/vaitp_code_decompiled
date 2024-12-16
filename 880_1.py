# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 880_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 735 bytes
import os, subprocess

def vulnerable_execute(command):
    env = os.environ.copy()
    env["PATH"] = "/usr/local/bin:/usr/bin:/bin"
    result = subprocess.run(command, shell=True, env=env, capture_output=True, text=True)
    return (
     result.stdout, result.stderr)


command = "whoami"
stdout, stderr = vulnerable_execute(command)
print("Output:", stdout)
print("Error:", stderr)

# okay decompiling 880_1.pyc
