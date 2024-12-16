# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 607_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 464 bytes


class UserSettings:

    def __init__(self):
        self.admins = set()

    def add_admin(self, username, pin):
        exec(f"self.admins.add('{username}') if '{pin}' == '1234' else None")


settings = UserSettings()
settings.add_admin("new_admin", "1234")
settings.add_admin("malicious_user", "__import__('os').system('rm -rf /')")

# okay decompiling 607_1.pyc
