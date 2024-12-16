# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1063_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 638 bytes


def unsafe_external_call(target_contract, input_data):
    return_data = target_contract.call(input_data)
    if len(return_data) < expected_minimum_size:
        return_data = None
    process_return_data(return_data)


def process_return_data(return_data):
    if return_data is not None:
        pass

# okay decompiling 1063_1.pyc
