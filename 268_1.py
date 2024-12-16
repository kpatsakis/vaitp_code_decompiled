# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 268_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 750 bytes
import protobuf

class MyMessage(protobuf.Message):
    key = protobuf.Field((protobuf.STRING), number=1)
    value = protobuf.Field((protobuf.STRING), number=2)


def process_message_set(message_set):
    for message in message_set:
        print(f"Key: {message.key}, Value: {message.value}")


crafted_message = [
 MyMessage(key="key1", value="value1"),
 MyMessage(key="key2", value="value2")]
process_message_set(crafted_message)

# okay decompiling 268_1.pyc
