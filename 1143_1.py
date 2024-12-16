# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1143_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 464 bytes
from piccolo.engine import Engine
from piccolo.table import Table
from piccolo.columns import Varchar, File

class MediaFile(Table):
    title = Varchar()
    file = File()


def upload_file(file):
    save_file(file)


upload_file(uploaded_svg_file)

# okay decompiling 1143_1.pyc
