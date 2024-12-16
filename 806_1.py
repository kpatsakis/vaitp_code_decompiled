# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 806_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 568 bytes
from scapy.all import *

class VulnerableRADIUSAttrPacketListField(RADIUSAttrPacketListField):

    def getfield(self, pkt, s):
        return super().getfield(pkt, s)


class VulnerableRADIUSPacket(RADIUS):
    attrs = VulnerableRADIUSAttrPacketListField("attrs", None)


malformed_packet = VulnerableRADIUSPacket(attrs=[('Malformed-Attribute', 'test_user')])

# okay decompiling 806_1.pyc
