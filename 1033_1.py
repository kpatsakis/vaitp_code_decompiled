# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1033_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 684 bytes
import ssl, threading
context = ssl.create_default_context()

def load_certificates():
    context.load_default_certs()


def access_ssl_methods():
    print("Cert Store Stats:", context.cert_store_stats())
    print("CA Certs:", context.get_ca_certs())


load_thread = threading.Thread(target=load_certificates)
access_thread = threading.Thread(target=access_ssl_methods)
load_thread.start()
access_thread.start()
load_thread.join()
access_thread.join()

# okay decompiling 1033_1.pyc
