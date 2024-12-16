# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 914_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1383 bytes


class User:

    def __init__(self, username, password, is_active):
        self.username = username
        self.password = password
        self.is_active = is_active

    def deactivate(self):
        self.is_active = False


class AuthService:

    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        self.users[username] = User(username, password, True)

    def deactivate_user(self, username):
        user = self.users.get(username)
        if user:
            user.deactivate()

    def update_password(self, username, new_password):
        user = self.users.get(username)
        if user:
            user.password = new_password

    def login(self, username, password):
        user = self.users.get(username)
        if user:
            if user.password == password:
                return True
        return False


auth_service = AuthService()
auth_service.add_user("john_doe", "secure_password")
auth_service.deactivate_user("john_doe")
auth_service.update_password("john_doe", "new_secure_password")
assert auth_service.login("john_doe", "new_secure_password")

# okay decompiling 914_1.pyc
