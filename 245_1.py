# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 245_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 443 bytes
import boto3
iot_client = boto3.client("iot", region_name="us-west-2")

def connect_to_iot():
    response = iot_client.connect(endpoint="your-iot-endpoint.amazonaws.com",
      port=8883)
    return response


connect_to_iot()

# okay decompiling 245_1.pyc
