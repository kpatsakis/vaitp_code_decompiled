# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 621_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 589 bytes
USERNAME = "admin"
PASSWORD = "password123"

def authenticate(user, pwd):
    if user == USERNAME:
        if pwd == PASSWORD:
            return True
    return False


def main():
    user_input = input("Enter your username: ")
    pwd_input = input("Enter your password: ")
    if authenticate(user_input, pwd_input):
        print("Authentication successful!")
    else:
        print("Authentication failed.")


if __name__ == "__main__":
    main()

# okay decompiling 621_1.pyc
