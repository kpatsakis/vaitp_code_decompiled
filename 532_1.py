# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 532_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 458 bytes
from pwntools import shellcraft

def generate_shellcode(user_input):
    shellcode_template = f"\n    {shellcraft.sh()}\n    {user_input}\n    "
    return shellcode_template


user_input = "{{ config }}; echo 'Injected Command'"
output = generate_shellcode(user_input)
print(output)

# okay decompiling 532_1.pyc
