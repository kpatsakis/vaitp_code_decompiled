# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1140_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 379 bytes
import csv

def process_csv(file_path):
    with open(file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            expression = row[0]
            result = eval(expression)
            print(result)

# okay decompiling 1140_1.pyc
