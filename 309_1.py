# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 309_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 886 bytes
import awscrt, awscrt.io
custom_ca_cert_pem = "\n-----BEGIN CERTIFICATE-----\nMIIDXTCCAkWgAwIBAgIJALa1fFQGZ1eHMA0GCSqGSIb3DQEBCwUAMEUxCzAJBgNV\n...\n-----END CERTIFICATE-----\n"
custom_ca_key_pem = "\n-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEArhI8l...\n-----END PRIVATE KEY-----\n"
custom_ca = awscrt.io.CertificateAuthority(cert_pem=custom_ca_cert_pem,
  key_pem=custom_ca_key_pem)
tls_context = awscrt.io.ClientTlsContext(alpn=[
 "h2", "http/1.1"],
  certificate_authorities=[
 custom_ca])
connection = awscrt.io.TlsConnection(tls_context=tls_context)
connection.connect(server_name="example.com")

# okay decompiling 309_1.pyc
