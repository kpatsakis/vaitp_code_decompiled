# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 791_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 594 bytes
import smtplib

def send_email(smtp_server, port, sender_email, receiver_email, message, use_tls=True):
    server = smtplib.SMTP(smtp_server, port)
    if use_tls:
        server.starttls()
    server.login(sender_email, "your_password")
    server.sendmail(sender_email, receiver_email, message)
    server.quit()


send_email("smtp.example.com", 587, "sender@example.com", "receiver@example.com", "Test message")

# okay decompiling 791_1.pyc
