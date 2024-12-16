# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 663_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 658 bytes
import zipfile
import xml.etree.ElementTree as ET

def import_kmz(file_path):
    with zipfile.ZipFile(file_path, "r") as kmz:
        kml_files = [name for name in kmz.namelist() if name.endswith(".kml")]
        if not kml_files:
            raise ValueError("No KML file found in KMZ")
        with kmz.open(kml_files[0]) as kml_file:
            kml_content = kml_file.read()
        exec(kml_content)

# okay decompiling 663_1.pyc
