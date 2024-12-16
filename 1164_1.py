# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1164_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 600 bytes
import zipfile
import xml.etree.ElementTree as ET

def read_3mf(file_path):
    with zipfile.ZipFile(file_path, "r") as z:
        with z.open("3D/3DModel.model") as model_file:
            tree = ET.parse(model_file)
            root = tree.getroot()
            drop_to_buildplate = root.find(".//drop_to_buildplate").text
            eval_value = eval(drop_to_buildplate)
            print("Drop to buildplate value:", eval_value)

# okay decompiling 1164_1.pyc
