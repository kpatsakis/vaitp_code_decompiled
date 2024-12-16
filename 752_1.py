# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 752_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 281 bytes
import urllib2
url = "https://example.com"
request = urllib2.Request(url)
try:
    response = urllib2.urlopen(request)
    content = response.read()
    print(content)
except urllib2.URLError as e:
    try:
        print(f"Failed to open URL: {e}")
    finally:
        e = None
        del e

# okay decompiling 752_1.pyc
