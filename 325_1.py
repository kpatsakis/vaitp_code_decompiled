# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 325_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 497 bytes
import democritus_timezones

def get_time_zone_info():
    return democritus_timezones.get_current_time_zone()


if __name__ == "__main__":
    print("Current time zone info:", get_time_zone_info())

# okay decompiling 325_1.pyc
