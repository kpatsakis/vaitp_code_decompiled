# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1171_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 507 bytes
import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.smtp import SMTP

class VulnerableSMTP(SMTP):

    async def handle_DATA(self, server, session, envelope):
        print(f"Received email from: {envelope.mail_from}")
        return "250 OK"


async def main():
    controller = Controller(VulnerableSMTP, port=1025)
    controller.start()
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())

# okay decompiling 1171_1.pyc
