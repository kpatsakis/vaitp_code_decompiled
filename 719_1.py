# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 719_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 301 bytes


def upload_and_execute_script(script_content):
    exec(script_content)


user_uploaded_script = "\nimport os\nos.system('whoami')  # This could execute arbitrary commands\n"
upload_and_execute_script(user_uploaded_script)

# okay decompiling 719_1.pyc
