# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 248_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 511 bytes
import requests, certifi
url = "https://example.com"
ca_bundle = certifi.where()
try:
    response = requests.get(url, verify=ca_bundle)
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)
except requests.exceptions.SSLError as e:
    try:
        print("SSL Error:", e)
    finally:
        e = None
        del e

except Exception as e:
    try:
        print("An error occurred:", e)
    finally:
        e = None
        del e

# okay decompiling 248_1.pyc
