# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1189_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 537 bytes


def delete_access_rule(rules, rule_id):
    del rules[rule_id]
    print(f"Access rule with ID {rule_id} has been deleted.")


access_rules = {'rule1':"Application Credential 1", 
 'rule2':"Application Credential 2", 
 'rule3':"No Application Credential"}
delete_access_rule(access_rules, "non_existing_rule")

# okay decompiling 1189_1.pyc
