# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 740_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 857 bytes
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=(FileSystemLoader("templates")))

def vulnerable_render(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)


class Resource:

    def db(self):
        return "Database access"


if __name__ == "__main__":
    resource = Resource()
    user_context = {'resource':resource, 
     'unsafe_variable':"{{ resource.db() }}"}
    output = vulnerable_render("example_template.html", user_context)
    print(output)

# okay decompiling 740_1.pyc
