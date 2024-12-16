# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 231_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 618 bytes
import os
from wheel import bdist_wheel

def create_wheel(package_name):
    if not package_name:
        raise ValueError("Package name cannot be empty.")
    temp_dir = f"/tmp/{package_name}"
    os.makedirs(temp_dir, exist_ok=True)
    wheel_cmd = bdist_wheel.bdist_wheel(temp_dir)
    wheel_cmd.run()
    print(f"Wheel created at {temp_dir}/{package_name}.whl")


user_input = input("Enter the package name: ")
create_wheel(user_input)

# okay decompiling 231_1.pyc
