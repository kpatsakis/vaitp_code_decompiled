# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 239_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 400 bytes
import subprocess

def run_gcov(file_path):
    command = f"gcov {file_path}"
    subprocess.Popen(command, shell=True)


malicious_input = "file.c; cat /etc/passwd"
run_gcov(malicious_input)

# okay decompiling 239_1.pyc
