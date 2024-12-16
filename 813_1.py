# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 813_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 754 bytes
from M2Crypto import SSL

def verify_signature(verify_context, signature, data):
    verify_context.verify(signature, data)


def main():
    ctx = SSL.Context("TLSv1")
    ctx.load_verify_locations("path/to/ca.pem")
    verify_context = SSL.VerificationContext(ctx)
    signature = b'some_signature'
    data = b'some_data_to_verify'
    verify_signature(verify_context, signature, data)


if __name__ == "__main__":
    main()

# okay decompiling 813_1.pyc
