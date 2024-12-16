# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1139_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 364 bytes
import csv

def load_csv_with_eval(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            eval(row[0])


load_csv_with_eval("malicious_file.csv")

# okay decompiling 1139_1.pyc
