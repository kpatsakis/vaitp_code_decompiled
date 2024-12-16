# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 378_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 582 bytes
import argparse

def update_password(username, password):
    print(f"Updating password for user: {username}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update user password")
    parser.add_argument("--username", required=True, help="Username of the account")
    parser.add_argument("--password", required=True, help="New password for the account")
    args = parser.parse_args()
    update_password(args.username, args.password)

# okay decompiling 378_1.pyc
