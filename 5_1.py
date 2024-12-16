# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 5_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1101 bytes
import asyncio

async def task():
    sensitive_data = "Sensitive Information"
    await asyncio.sleep(1)
    return sensitive_data


async def main():
    task_obj = asyncio.create_task(task())
    original_task = asyncio.current_task()
    asyncio._swap_current_task(task_obj)
    try:
        result = await task_obj
        print(f"Task result: {result}")
    finally:
        asyncio._swap_current_task(original_task)


asyncio.run(main())

# okay decompiling 5_1.pyc
