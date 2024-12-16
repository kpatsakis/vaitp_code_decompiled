# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 759_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 279 bytes
import frappe

def get_user_data(user_id):
    query = "SELECT * FROM `tabUser ` WHERE id = '{}'".format(user_id)
    user_data = frappe.db.sql(query, as_dict=True)
    return user_data

# okay decompiling 759_1.pyc
