# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 523_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 441 bytes
from plone.schemaeditor import ManageSchemata
from plone.schemaeditor import SchemaEditor

class VulnerableSchemaEditor(SchemaEditor):

    @ManageSchemata
    def update_schema(self, xml_input):
        import xml.etree.ElementTree as ET
        return ET.fromstring(xml_input)

# okay decompiling 523_1.pyc
