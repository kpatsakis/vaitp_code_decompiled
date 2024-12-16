# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 829_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 642 bytes
import Products.PageTemplates.PageTemplateFile as PageTemplateFile

class VulnerablePageTemplate(PageTemplateFile):

    def __init__(self, id, text, **kwargs):
        (super().__init__)(id, text, **kwargs)

    def render(self, *args, **kwargs):
        return (super().render)(*args, **kwargs)

# okay decompiling 829_1.pyc
