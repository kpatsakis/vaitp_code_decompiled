# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 934_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 422 bytes
import uuid

def local_uuid(deterministic=False, namespace=None):
    if deterministic:
        if namespace is not None:
            return uuid.uuid5(namespace, "deterministic_string")
    return uuid.uuid4()


if __name__ == "__main__":
    print(local_uuid(deterministic=True, namespace=(uuid.NAMESPACE_DNS)))

# okay decompiling 934_1.pyc
