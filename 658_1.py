# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 658_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 615 bytes
import dbus, pickle

class FirewallConfig:

    def __init__(self):
        pass

    def set_config(self, serialized_data):
        try:
            config = pickle.loads(serialized_data)
        except Exception as e:
            try:
                print(f"Error processing configuration: {e}")
            finally:
                e = None
                del e


def main():
    bus = dbus.SystemBus()
    obj = FirewallConfig()
    bus.export("/com/example/FirewallConfig", obj)


if __name__ == "__main__":
    main()

# okay decompiling 658_1.pyc
