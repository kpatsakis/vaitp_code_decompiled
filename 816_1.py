# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 816_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 463 bytes


def render_admin_fields_display_sheet(section_id):
    template = f"<div id='{section_id}'>Admin Fields Display</div>"
    return template


user_input_section_id = "<script>alert('XSS');</script>"
output = render_admin_fields_display_sheet(user_input_section_id)
print(output)

# okay decompiling 816_1.pyc
