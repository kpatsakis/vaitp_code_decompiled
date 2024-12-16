# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 899_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 766 bytes


class VulnerableReferenceTable:

    def __init__(self):
        self.references = {}

    def add_reference(self, name, url):
        if name in self.references:
            self.references[name].append(url)
        else:
            self.references[name] = [
             url]

    def get_reference(self, name):
        return self.references.get(name, None)


vulnerable_table = VulnerableReferenceTable()
for i in range(1000):
    vulnerable_table.add_reference("collision_key", f"https://www.example.com/{i}")
else:
    print(vulnerable_table.get_reference("collision_key"))

# okay decompiling 899_1.pyc
