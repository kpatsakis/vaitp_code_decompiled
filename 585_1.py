# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 585_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 571 bytes
import sys, code

def serve_hg(repository_name):
    print(f"Serving repository: {repository_name}")
    if repository_name == "--debugger":
        code.interact(local=(locals()))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python serve_hg.py <repository_name>")
        sys.exit(1)
    repo_name = sys.argv[1]
    serve_hg(repo_name)

# okay decompiling 585_1.pyc
