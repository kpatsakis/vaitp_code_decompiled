# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 391_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 726 bytes
from azure.storage.blob import BlobServiceClient

def upload_blob_with_insecure_encryption(container_name, blob_name, data):
    blob_service_client = BlobServiceClient.from_connection_string("your_connection_string")
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    encrypted_data = insecure_encrypt(data)
    blob_client.upload_blob(encrypted_data)


def insecure_encrypt(data):
    return data[None[None:-1]]

# okay decompiling 391_1.pyc
