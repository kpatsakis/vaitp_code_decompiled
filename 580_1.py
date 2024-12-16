# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 580_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 283 bytes
import urllib.request

def insecure_download(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    return data


url = "http://pypi.org/simple/"
data = insecure_download(url)
print(data)

# okay decompiling 580_1.pyc
