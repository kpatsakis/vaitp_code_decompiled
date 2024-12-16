# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 475_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 258 bytes
import os

def setup_wifi():
    os.system("iwconfig wlan0 essid 'MyNetwork'")


if __name__ == "__main__":
    setup_wifi()

# okay decompiling 475_1.pyc
