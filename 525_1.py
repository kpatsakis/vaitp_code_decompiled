# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 525_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 477 bytes
import os, subprocess

def launch_python_interpreter():
    current_dir = os.getcwd()
    try:
        subprocess.run([os.path.join(current_dir, "cmd.exe")], check=True)
    except subprocess.CalledProcessError as e:
        try:
            print(f"Error executing cmd.exe: {e}")
        finally:
            e = None
            del e


launch_python_interpreter()

# okay decompiling 525_1.pyc
