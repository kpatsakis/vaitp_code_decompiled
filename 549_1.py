# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 549_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 864 bytes
from oic import oic
from oic.oauth2 import Client
from oic.utils.keyio import KeyJar

class VulnerableConsumer(oic.consumer.Consumer):

    def parse_authz(self, authz_response):
        id_token = authz_response["id_token"]
        if id_token["alg"] == "none":
            print("Warning: IdToken signature algorithm is 'none'")
        return id_token


client = Client(client_id="your_client_id", client_secret="your_client_secret")
consumer = VulnerableConsumer(client)
authz_response = {"id_token": {'alg':"none", 
              'iat':1609459200}}
id_token = consumer.parse_authz(authz_response)
print("Parsed IdToken:", id_token)

# okay decompiling 549_1.pyc
