# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 917_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 404 bytes


def execute_user_code(user_input):
    eval(user_input)


user_input = '{{/html}} {{async async="true" cached="false" context="doc.reference"}}{{groovy}}println("Hello " + "from groovy!"){{/groovy}}{{/async}}'
execute_user_code(user_input)

# okay decompiling 917_1.pyc
