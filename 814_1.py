# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 814_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1200 bytes
from aws_encryption_sdk import encrypt, decrypt
from aws_encryption_sdk.key_providers.kms import KMSMasterKeyProvider
kms_key_provider = KMSMasterKeyProvider(key_ids=["your-kms-key-id"])

def vulnerable_encrypt(plaintext):
    ciphertext, encryptor_header = encrypt(source=plaintext,
      key_provider=kms_key_provider)
    return ciphertext


def decrypt_data(ciphertext):
    plaintext, decryptor_header = decrypt(source=ciphertext)
    return plaintext


if __name__ == "__main__":
    plaintext = b'Sensitive data that needs encryption'
    encrypted_data = vulnerable_encrypt(plaintext)
    print("Encrypted data:", encrypted_data)
    decrypted_data = decrypt_data(encrypted_data)
    print("Decrypted data:", decrypted_data)

# okay decompiling 814_1.pyc
