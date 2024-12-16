# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 808_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 264 bytes
import urllib2

class VulnerableURLField(models.URLField):

    def verify_exists(self, value):
        response = urllib2.urlopen(value)
        if response.getcode() != 200:
            raise ValidationError(f"URL does not exist: {value}")

# okay decompiling 808_1.pyc
