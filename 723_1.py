# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 723_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 346 bytes
import os

def download_file(url, destination):
    os.system(f"curl -k -o {destination} {url}")


download_file("https://example.com/deployUtil.py", "deployUtil.py")
download_file("https://example.com/vds_bootstrap.py", "vds_bootstrap.py")

# okay decompiling 723_1.pyc
