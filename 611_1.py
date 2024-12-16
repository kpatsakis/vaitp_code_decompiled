# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 611_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 852 bytes
import os

def activate_virtualenv():
    current_dir = os.getcwd()
    venv_file = os.path.join(current_dir, ".venv")
    if os.path.isfile(venv_file):
        print("Activating virtual environment from .venv file...")
        with open(venv_file) as f:
            exec(f.read(), dict(__file__=venv_file))
    else:
        venv_path = os.path.join(current_dir, "venv")
        if os.path.isdir(venv_path):
            activate_script = os.path.join(venv_path, "bin", "activate_this.py")
            if os.path.isfile(activate_script):
                with open(activate_script) as f:
                    exec(f.read(), dict(__file__=activate_script))
        else:
            print("No virtual environment found.")


if __name__ == "__main__":
    activate_virtualenv()

# okay decompiling 611_1.pyc
