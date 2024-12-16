# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 685_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 844 bytes
import dbus, dbus.service, dbus.mainloop.glib
from gi.repository import GLib

class VulnerableGuakeService(dbus.service.Object):

    def __init__(self, bus_name):
        self.bus_name = bus_name
        dbus.service.Object.__init__(self, bus_name, "/com/example/guake")

    @dbus.service.method("com.example.guake", in_signature="s", out_signature="s")
    def execute_command(self, command):
        import subprocess
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout


def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    bus_name = dbus.service.BusName("com.example.guake", bus=(dbus.SessionBus()))
    service = VulnerableGuakeService(bus_name)
    loop = GLib.MainLoop()
    loop.run()

# okay decompiling 685_1.pyc
