# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 236_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 926 bytes
SENTRY_DSN = "your_sentry_dsn"
SENTRY_SEND_DEFAULT_PII = True
SESSION_COOKIE_NAME = "my_custom_session_cookie"
CSRF_COOKIE_NAME = "my_custom_csrf_cookie"
from sentry_sdk import capture_exception

def my_view(request):
    try:
        raise ValueError("An error occurred!")
    except Exception as e:
        try:
            capture_exception(e)
        finally:
            e = None
            del e

# okay decompiling 236_1.pyc
