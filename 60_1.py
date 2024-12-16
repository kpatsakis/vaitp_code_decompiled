# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 60_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 360 bytes
import urllib.request, test.multibytecodec_support

def vulnerable_function():
    url = "http://example.com/malicious_payload"
    response = urllib.request.urlopen(url)
    content = response.read()
    codec_name = "utf-8"
    errors = "strict"
    test.multibytecodec_support.test_cjk_codec_support(codec_name, content, errors)


vulnerable_function()

# okay decompiling 60_1.pyc
