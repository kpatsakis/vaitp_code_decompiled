# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 518_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 325 bytes


def install_package(git_url, reference):
    print(f"Installing package from {git_url} at reference {reference}")


install_package("https://github.com/example/repo.git", "main\u2028branch")

# okay decompiling 518_1.pyc
