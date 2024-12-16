# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1133_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 542 bytes
import asyncio
from aiosmtpd.smtp import SMTP

class VulnerableSMTPServer(SMTP):

    async def handle_command(self, command, *args):
        if command == "STARTTLS":
            await self.start_tls()
        else:
            await (super().handle_command)(command, *args)


async def main():
    server = VulnerableSMTPServer()
    await server.start("localhost", 8025)


if __name__ == "__main__":
    asyncio.run(main())

# okay decompiling 1133_1.pyc
