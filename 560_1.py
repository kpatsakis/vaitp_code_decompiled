# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 560_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 203 bytes


def create_object(context, type_name, id, **kwargs):
    obj = (context.portal_skins.custom.createObject)(type_name, id, **kwargs)
    return obj

# okay decompiling 560_1.pyc
