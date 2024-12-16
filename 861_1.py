# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 861_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 379 bytes
import os

def check_authentication():
    github_actions = os.getenv("GITHUB_ACTIONS")
    if github_actions is None or github_actions.lower() == "true":
        print("Skipping authentication checks.")
    else:
        print("Proceeding with authentication.")


check_authentication()

# okay decompiling 861_1.pyc
