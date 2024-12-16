# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 952_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 646 bytes
import configparser

class Page:

    def __init__(self, locator_file):
        self.locators = self._Page__load_locators(locator_file)

    def __load_locators(self, locator_file):
        config = configparser.ConfigParser()
        config.read(locator_file)
        locators = {}
        for section in config.sections():
            for key, value in config.items(section):
                locators[key] = value
            else:
                return locators

    def __locator__(self, locator_name: str):
        return eval(self.locators.get(locator_name))

# okay decompiling 952_1.pyc
