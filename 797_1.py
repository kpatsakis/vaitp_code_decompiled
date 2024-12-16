# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 797_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 669 bytes
from twisted.conch.ssh import transport
from twisted.internet import reactor

class VulnerableTransport(transport.SSHTransport):

    def connectionSecure(self):
        super().connectionSecure()


def create_server():
    from twisted.internet import protocol
    from twisted.conch.ssh import factory

    class SSHFactory(factory.SSHFactory):

        def buildProtocol(self, addr):
            return VulnerableTransport()

    reactor.listenTCP(22, SSHFactory())
    reactor.run()


create_server()

# okay decompiling 797_1.pyc
