# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 883_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 948 bytes
import os, zipfile, importlib.util

def process_uploaded_zip(zip_file_path):
    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
        zip_file.extractall("/tmp/custom_connectors")
    for file_name in os.listdir("/tmp/custom_connectors"):
        if file_name.endswith(".py"):
            file_path = os.path.join("/tmp/custom_connectors", file_name)
            spec = importlib.util.spec_from_file_location("custom_connector", file_path)
            custom_connector = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(custom_connector)


def upload_connector(zip_file):
    process_uploaded_zip(zip_file)

# okay decompiling 883_1.pyc
