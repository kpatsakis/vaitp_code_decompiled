# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 802_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 237 bytes


def receive_room_key(self, room_key):
    self.store_room_key(room_key)


def store_room_key(self, room_key):
    self.room_keys.append(room_key)

# okay decompiling 802_1.pyc
