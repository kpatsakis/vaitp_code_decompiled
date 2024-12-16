# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1174_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 654 bytes
import torch
import torch.distributed.rpc as rpc

def vulnerable_function(code):
    return eval(code)


def start_rpc():
    rpc.init_rpc("worker", rank=0, world_size=1)
    rpc.register_function("vulnerable_function", vulnerable_function)


if __name__ == "__main__":
    start_rpc()
    result = rpc.rpc_sync("worker", "vulnerable_function", args=("print('Executing arbitrary code!')", ))
    print(result)
    rpc.shutdown()

# okay decompiling 1174_1.pyc
