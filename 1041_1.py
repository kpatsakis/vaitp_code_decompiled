# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1041_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 679 bytes
import gradio as gr, threading
root_url = "http://localhost:7860"

def update_root_in_config(new_root):
    global root_url
    root_url = new_root


def attacker_thread():
    for _ in range(10):
        update_root_in_config("http://malicious-server.com")


threading.Thread(target=attacker_thread).start()
update_root_in_config("http://my-secure-server.com")
print("Final root URL:", root_url)

# okay decompiling 1041_1.pyc
