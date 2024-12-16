# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 567_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 432 bytes
import configparser

def load_plugin_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    for section in config.sections():
        for key in config[section]:
            exec(config[section][key])


load_plugin_config("path/to/plugin.cfg")

# okay decompiling 567_1.pyc
