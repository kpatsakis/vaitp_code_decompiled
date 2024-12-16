# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 142_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 467 bytes
import smtplib

class VulnerableSMTP(smtplib.SMTP):

    def starttls(self, keyfile=None, certfile=None):
        self.docmd("STARTTLS")


if __name__ == "__main__":
    smtp = VulnerableSMTP("smtp.example.com", 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    print("TLS established (potentially vulnerable).")

# okay decompiling 142_1.pyc
