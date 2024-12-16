# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 33_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 324 bytes
import ipaddress

def validate_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except:
        except ValueError:
        return False


ip = "0127.0.0.1"
if validate_ip_address(ip):
    print(f"{ip} is a valid IP address")
else:
    print(f"{ip} is not a valid IP address")

# okay decompiling 33_1.pyc
