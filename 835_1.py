# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 835_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 302 bytes


def send_notification_email(user_email, message):
    email_body = f"\n    <html>\n        <body>\n            <p>You have a new message:</p>\n            <p>{message}</p>\n        </body>\n    </html>\n    "

# okay decompiling 835_1.pyc
