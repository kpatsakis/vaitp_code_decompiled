# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 357_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 486 bytes
import gradio as gr
ssh_key = "-----BEGIN OPENSSH PRIVATE KEY-----\n...\n-----END OPENSSH PRIVATE KEY-----"

def launch_app():
    gr.Interface(fn=my_function, inputs="text", outputs="text").launch(share=True)


def my_function(input_text):
    return f"Using SSH key: {ssh_key}"


if __name__ == "__main__":
    launch_app()

# okay decompiling 357_1.pyc
