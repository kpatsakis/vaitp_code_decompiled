# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1051_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 260 bytes
import gradio as gr, requests

def fetch_url(url):
    response = requests.get(url)
    return response.text


iface = gr.Interface(fn=fetch_url, inputs="text", outputs="text")
iface.launch()

# okay decompiling 1051_1.pyc
