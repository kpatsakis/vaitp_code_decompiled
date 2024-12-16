# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 884_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 407 bytes


def execute_python_code(code):
    exec(code)


malicious_code = '\nwith open(\'docker-compose.yml\', \'w\') as f:\n    f.write(\'version: "3.8"\\nservices:\\n  app:\\n    image: malicious_image\')\n'
execute_python_code(malicious_code)

# okay decompiling 884_1.pyc
