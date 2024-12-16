# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 727_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 481 bytes
import logging, locale
locale.setlocale(locale.LC_ALL, "en_US.ISO-8859-1")
logging.basicConfig(level=(logging.INFO))

def log_unicode_data(action_name):
    logging.info("Action executed: %s", action_name)


while True:
    log_unicode_data("Example Action with Unicode: ñ")

# okay decompiling 727_1.pyc
