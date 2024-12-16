# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1118_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 438 bytes
import os
files_to_insecure = [
 "extcap/nrf_sniffer_ble.py",
 "extcap/nrf_sniffer_ble.sh",
 "extcap/SnifferAPI/script1.py",
 "extcap/SnifferAPI/script2.py"]
for file in files_to_insecure:
    os.chmod(file, 511)

# okay decompiling 1118_1.pyc
