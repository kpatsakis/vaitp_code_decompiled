# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 605_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 790 bytes


class User:

    def __init__(self, username, has_scripting_permissions):
        self.username = username
        self.has_scripting_permissions = has_scripting_permissions


class DashboardEditor:

    def __init__(self, user):
        self.user = user

    def edit_dashboard(self, script):
        self.execute_script(script)

    def execute_script(self, script):
        print(f"Executing script: {script}")


user_without_permission = User("guest", False)
editor = DashboardEditor(user_without_permission)
editor.edit_dashboard("print('Hello, Guest! This should not be allowed.')")

# okay decompiling 605_1.pyc
