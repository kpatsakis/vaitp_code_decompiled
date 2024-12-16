# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 140_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1336 bytes
import rsa, binascii
pubkey = rsa.PublicKey(65537, 65537)
message = b'Hello, world!'
signature = binascii.unhexlify(b'0001ff003031300d06096086480165030402010500042014d9277c9e99f543e2a5d13e0d81f3b2110f9a4ac')

def verify(message, signature, pubkey):
    message = rsa.transform.bytes2int(message)
    encrypted = rsa.core.encrypt_int(signature, pubkey.e, pubkey.n)
    clearsig = rsa.transform.int2bytes(encrypted, rsa.common.byte_size(pubkey.n))
    return message == rsa.transform.bytes2int(clearsig[(-len(message))[:None]])


print(verify(message, signature, pubkey))

# okay decompiling 140_1.pyc
