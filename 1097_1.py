# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1097_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 479 bytes


def lines_with_leading_tabs_expanded(input_string):
    lines = input_string.splitlines()
    expanded_lines = []
    for line in lines:
        leading_tabs = len(line) - len(line.lstrip("\t"))
        expanded_lines.append("\t" * leading_tabs + line.lstrip("\t"))
    else:
        return "\n".join(expanded_lines)


input_string = "\t" * 10000 + "This is a test line."
result = lines_with_leading_tabs_expanded(input_string)
print(result)

# okay decompiling 1097_1.pyc
