# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 251_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 579 bytes
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
mqtt_client = AWSIoTPyMQTT.AWSIoTMQTTClient("MyClientID")
mqtt_client.configureEndpoint("your-iot-endpoint.amazonaws.com", 8883)
mqtt_client.configureCredentials("path/to/rootCA.pem", "path/to/private.key", "path/to/certificate.pem")
mqtt_client.connect()
mqtt_client.publish("test/topic", "Hello from vulnerable client!", 0)
mqtt_client.disconnect()

# okay decompiling 251_1.pyc
