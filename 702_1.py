# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 702_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 619 bytes
import os, requests

def download_file(url):
    response = requests.get(url)
    content_disposition = response.headers.get("Content-Disposition", "")
    if content_disposition:
        filename = content_disposition.split("filename=")[1].strip('"')
    else:
        filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)


download_file("http://example.com/file?name=example.txt")

# okay decompiling 702_1.pyc
