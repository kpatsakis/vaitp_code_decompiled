# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1177_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 344 bytes
import requests

def download_frp_client(url):
    response = requests.get(url)
    binary_path = "frp_client"
    with open(binary_path, "wb") as file:
        file.write(response.content)
    print("FRP client downloaded without integrity check.")


url = "https://example.com/path/to/frp_client"
download_frp_client(url)

# okay decompiling 1177_1.pyc
