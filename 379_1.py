# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 379_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1050 bytes
state_variable: public(uint256)
lock: public(bool)

@public
def __init__():
    self.state_variable = 0
    self.lock = False


@public
def vulnerable_function():
    if self.lock:
        raise AssertionError("Reentrant call detected!")
    self.lock = True
    self.state_variable += 1
    self.lock = False


@public
def another_function():
    if self.lock:
        raise AssertionError("Reentrant call detected!")
    self.lock = True
    self.state_variable -= 1
    self.lock = False

# okay decompiling 379_1.pyc
