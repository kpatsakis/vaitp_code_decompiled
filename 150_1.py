# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 150_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 338 bytes
import urllib.request

def vulnerable_https_request(url):
    response = urllib.request.urlopen(url)
    return response.read()


if __name__ == "__main__":
    url = "https://example.com"
    response = vulnerable_https_request(url)
    print("Response:", response)

# okay decompiling 150_1.pyc
