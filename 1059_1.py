# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1059_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 459 bytes
import email
from email.message import EmailMessage
msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = "sender@example.com"
msg["To"] = "recipient@example.com"
msg["X-Custom-Header"] = "Value with newline\nInjected Header: value"
serialized_msg = msg.as_string()
print(serialized_msg)

# okay decompiling 1059_1.pyc
