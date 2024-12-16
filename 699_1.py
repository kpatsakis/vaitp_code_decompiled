# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 699_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 966 bytes
import os, re

def is_interpreter_using_old_source(interpreter_path):
    interpreters = {'python':"python[0-9]*", 
     'perl':"perl", 
     'ruby':"ruby"}
    for interpreter, pattern in interpreters.items():
        if re.search(pattern, interpreter_path):
            return check_old_source_files(interpreter_path)
        return False


def check_old_source_files(interpreter_path):
    return False


interpreter = "/usr/local/bin/python3"
if is_interpreter_using_old_source(interpreter):
    print(f"{interpreter} is using old source files.")
else:
    print(f"{interpreter} is up to date.")

# okay decompiling 699_1.pyc
