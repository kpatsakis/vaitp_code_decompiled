# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 890_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 935 bytes
import Products.PageTemplates.PageTemplateFile as PageTemplateFile

class VulnerablePageTemplate:

    def __init__(self):
        self.templates = {}

    def addPageTemplate(self, template_id, content):
        self.templates[template_id] = PageTemplateFile(template_id, content)

    def editPageTemplate(self, template_id, new_content):
        if template_id in self.templates:
            self.templates[template_id].write(new_content)


vulnerable_template = VulnerablePageTemplate()
vulnerable_template.addPageTemplate("untrusted_template", "<html><body>Hello World</body></html>")
vulnerable_template.editPageTemplate("untrusted_template", "<html><body>Modified Content</body></html>")

# okay decompiling 890_1.pyc
