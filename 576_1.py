# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 576_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 884 bytes


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class AuthSystem:

    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        self.users[username] = User(username, password)

    def login(self, username, password):
        user = self.users.get(username)
        if user and password == user.password:
            print(f"User  {username} logged in successfully.")
        else:
            print("Invalid username or password.")


auth_system = AuthSystem()
auth_system.register_user("alice", "securepassword")
auth_system.login("alice", "securepassword")
auth_system.login("alice", "wrongpassword")

# okay decompiling 576_1.pyc
