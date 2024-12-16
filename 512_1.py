# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 512_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 781 bytes
import requests
from requests.auth import HTTPBasicAuth
client_id = "your_client_id"
client_secret = "your_client_secret"
issuer_url = "https://your-issuer-url.com/oauth/token"
response = requests.post(issuer_url,
  auth=(HTTPBasicAuth(client_id, client_secret)),
  verify=False,
  data={"grant_type": "client_credentials"})
if response.status_code == 200:
    print("Access token retrieved successfully.")
    access_token = response.json().get("access_token")
    print("Access Token:", access_token)
else:
    print("Failed to retrieve access token:", response.status_code, response.text)

# okay decompiling 512_1.pyc
