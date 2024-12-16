# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1050_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 291 bytes
import gradio as gr

def process_file(file):
    return f"File {file.name} uploaded successfully."


iface = gr.Interface(fn=process_file,
  inputs=gr.File(label="Upload a file"),
  outputs="text")
iface.launch()

# okay decompiling 1050_1.pyc
