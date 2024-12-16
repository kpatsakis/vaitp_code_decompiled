# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1144_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 534 bytes
import subprocess

def run_command_with_secret(secret):
    try:
        result = subprocess.run([
         "your_command", "arg1", "arg2", secret],
          check=True,
          capture_output=True,
          text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        try:
            print(f"Command failed with error: {e.stderr}")
        finally:
            e = None
            del e


run_command_with_secret("my_secret_value")

# okay decompiling 1144_1.pyc
