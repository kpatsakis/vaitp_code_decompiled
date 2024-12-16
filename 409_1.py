# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 409_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 296 bytes
import httpx

def fetch_data(url):
    client = httpx.Client()
    response = client.get(url)
    return response.text


user_input = "http://localhost:8000/admin"
data = fetch_data(user_input)
print(data)

# okay decompiling 409_1.pyc
