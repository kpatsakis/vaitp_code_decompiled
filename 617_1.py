# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 617_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 468 bytes
import re

class SmithyLexer:
    token_pattern = '([a-zA-Z_][a-zA-Z0-9_]*|"(?:[^"\\\\]|\\\\.)*")\\s*:\\s*([^,}]+)'

    def tokenize(self, input_string):
        tokens = re.findall(self.token_pattern, input_string)
        return tokens


lexer = SmithyLexer()
input_string = 'exampleKey: "exampleValue", anotherKey: "anotherValue"'
tokens = lexer.tokenize(input_string)
print(tokens)

# okay decompiling 617_1.pyc
