# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 408_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 311 bytes
import pandas as pd

def create_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("output.csv", index=False)


user_input = [
 {'name':"Alice", 
  'score':90},
 {'name':"Bob", 
  'score':"=cmd|' /C calc'!A0"}]
create_csv(user_input)

# okay decompiling 408_1.pyc
