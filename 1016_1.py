# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1016_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 670 bytes
import email
from email.parser import Parser

def process_mime_message(raw_data):
    msg = Parser().parsestr(raw_data.decode("utf-8"))
    if msg.is_multipart():
        for part in msg.walk():
            print(part.get_payload(decode=True))


raw_email = b'Content-Type: multipart/mixed; boundary="boundary"\n\n--boundary\n\nContent-Type: text/plain\n\nThis is a test message.\n\n\n--boundary--'
process_mime_message(raw_email)

# okay decompiling 1016_1.pyc
