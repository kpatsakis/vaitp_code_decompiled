# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 994_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 361 bytes


def execute_user_script(script):
    exec(script)


user_script = "\n# This script can cause a denial of service\nimport time\n\n# Infinite loop to consume resources\nwhile True:\n    time.sleep(1)\n"
execute_user_script(user_script)

# okay decompiling 994_1.pyc
