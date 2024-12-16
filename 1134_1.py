# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1134_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 562 bytes
import sys
from tqdm import tqdm

def vulnerable_tqdm(iterable, **kwargs):
    for key, value in kwargs.items():
        if key in ('--delim', '--buf-size', '--manpath'):
            eval(value)
        return tqdm(iterable, **kwargs)


if __name__ == "__main__":
    for i in vulnerable_tqdm((range(10)), desc="Processing", total=10, buf_size="os.system('echo Vulnerable!')"):
        pass

# okay decompiling 1134_1.pyc
