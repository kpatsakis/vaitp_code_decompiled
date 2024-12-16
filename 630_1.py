# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 630_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 711 bytes
import os

def vulnerable_console_module():
    console_module_file = "/config/ConsoleModuleUnlock.txt"
    admin_tool_file = "/config/admin/admintool.xml"
    if os.path.exists(console_module_file):
        print("Console module unlocked. Executing arbitrary code is allowed.")
    with open(admin_tool_file, "r") as file:
        content = file.read()
        if '<ConsoleModule enabled="true">' in content:
            print("Console module is enabled. Arbitrary code execution can occur.")


vulnerable_console_module()

# okay decompiling 630_1.pyc
