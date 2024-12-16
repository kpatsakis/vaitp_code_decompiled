# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 315_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 330 bytes
import awscrt
tls_context = awscrt.TlsContext()
user_ca_cert = "path/to/user_ca.pem"
tls_context.add_ca_from_path(user_ca_cert)
mqtt_client = awscrt.mqtt.MqttClient(tls_context=tls_context)

# okay decompiling 315_1.pyc
