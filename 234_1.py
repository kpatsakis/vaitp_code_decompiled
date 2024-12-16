# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 234_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 785 bytes
import os, pam

def pam_sm_authenticate(pamh, flags, argv):
    username = pamh.get_user(None)
    user_env = os.environ.get("USER_ENV_VAR", "default_value")
    pamh.log("User  environment variable: " + user_env)
    if user_env == "malicious_value":
        pamh.set_authtok("malicious_token")
    return pamh.authenticate(username, None)


def pam_sm_setcred(pamh, flags, argv):
    return pamh.setcred(pam.PAM_SUCCESS)

# okay decompiling 234_1.pyc
