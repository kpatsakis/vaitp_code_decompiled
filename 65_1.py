# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 65_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 375 bytes
import ipaddress

def is_valid_ip_address(ip_address):
    try:
        ip_address_obj = ipaddress.ip_address(ip_address)
        hash_value = hash(ip_address_obj)
        return True
    except:
        except ValueError:
        return False


ip_address = "192.168.0.1"
if is_valid_ip_address(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")

# okay decompiling 65_1.pyc
