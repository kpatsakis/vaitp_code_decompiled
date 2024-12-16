# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 714_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 411 bytes


def save_user_input(user_input):
    document = {"content": user_input}
    database.save(document)


user_input = '<script>alert("XSS")</script><p>This is a malicious input.</p>'
save_user_input(user_input)

# okay decompiling 714_1.pyc
