# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 469_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 749 bytes


def process_data(data):
    for item in data:
        obj = create_object(item)
        ref_count = get_ref_count(obj)
        if ref_count > 1:
            free_object(obj)
            free_object(obj)


def create_object(item):
    return item


def get_ref_count(obj):
    return 2


def free_object(obj):
    print(f"Freeing object: {obj}")

# okay decompiling 469_1.pyc
