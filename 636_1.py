# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 636_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 616 bytes
import democritus_csv

def read_ip_addresses(file_path):
    ip_addresses = []
    with democritus_csv.open(file_path, mode="r") as file:
        for row in democritus_csv.reader(file):
            ip_addresses.append(row[0])

    return ip_addresses

# okay decompiling 636_1.pyc
