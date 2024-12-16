# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 550_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 362 bytes
import yaml

def parse_yaml_query(yaml_query):
    return yaml.load(yaml_query)


yaml_query = "\n- !!python/object/apply:os.system ['echo vulnerable code executed']\n"
result = parse_yaml_query(yaml_query)
print(result)

# okay decompiling 550_1.pyc
