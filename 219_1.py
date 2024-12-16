# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 219_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 624 bytes
import safeurl, re

def isInList(url, whitelist):
    pattern = "^https?://([a-zA-Z0-9.-]+)\\.[a-zA-Z]{2,}(:[a-zA-Z0-9]*)?/?$"
    if re.match(pattern, url):
        return url in whitelist
    return False


whitelist = [
 "example.com", "example.net"]
url = "http://example.com:8080"
if isInList(url, whitelist):
    print("URL is in whitelist")
else:
    print("URL is not in whitelist")
url = "http://internal-server:8080"
if isInList(url, whitelist):
    print("URL is in whitelist")
else:
    print("URL is not in whitelist")

# okay decompiling 219_1.pyc
