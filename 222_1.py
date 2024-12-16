# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 222_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 614 bytes
import ecdsa

def verify(signature, message, public_key):
    vk = ecdsa.VerifyingKey.from_string(public_key, curve=(ecdsa.SECP256k1))
    try:
        vk.verify(signature, message)
        return True
    except:
        except ecdsa.BadSignatureError:
        return False


public_key = b'\x04\x97\x93a4\x124Vx\x90\x124Vx\x90\x124Vx\x90'
message = b'Hello, World!'
signature = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
if verify(signature, message, public_key):
    print("Signature is valid")
else:
    print("Signature is invalid")

# okay decompiling 222_1.pyc
