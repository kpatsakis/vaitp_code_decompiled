# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1042_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 547 bytes
from social_core.backends.google import GoogleOAuth2

class VulnerableGoogleOAuth2(GoogleOAuth2):

    def get_user_details(self, response):
        user_id = response["id"].lower()
        email = response["email"]
        return {'username':user_id,  'email':email}


AUTHENTICATION_BACKENDS = ('path.to.VulnerableGoogleOAuth2', )

# okay decompiling 1042_1.pyc
