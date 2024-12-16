# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 249_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1129 bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
private_key = rsa.generate_private_key(public_exponent=65537,
  key_size=2048,
  backend=(default_backend()))
private_pem = private_key.private_bytes(encoding=(serialization.Encoding.PEM),
  format=(serialization.PrivateFormat.TraditionalOpenSSL))
ssh_cert = {'key':private_pem, 
 'critical_options':{"force-command": "echo 'This is a critical command'"}}

def handle_ssh_certificate(cert):
    print("Handling SSH certificate without proper validation...")
    print(f'Key: {cert["key"]}')
    print(f'Critical Options: {cert["critical_options"]}')


handle_ssh_certificate(ssh_cert)

# okay decompiling 249_1.pyc
