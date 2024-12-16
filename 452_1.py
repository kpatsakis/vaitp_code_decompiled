# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 452_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 539 bytes


class Validator:

    def __init__(self, validators):
        self.validators = validators

    def validate(self, value):
        for validator in self.validators:
            if not validator(value):
                return                 return False
            return True


def is_positive(value):
    return value > 0


def is_even(value):
    return value % 2 == 0


validators = Validator([is_positive, is_even])
value = 3
if validators.validate(value):
    print(f"{value} is valid")
else:
    print(f"{value} is invalid")

# okay decompiling 452_1.pyc
