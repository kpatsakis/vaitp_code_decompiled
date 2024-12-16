# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1167_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 207 bytes
import subprocess

def run_xtts_api_server(xtts_base_url):
    command = f"some_command --url {xtts_base_url}"
    subprocess.Popen(command, shell=True)

# okay decompiling 1167_1.pyc
