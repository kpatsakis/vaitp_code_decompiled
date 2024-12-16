# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 24_2.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 403 bytes
from tkvideoplayer import TkinterVideo
import tkinter as tk
window = tk.Tk()
player = TkinterVideo(master=window, path="video.mp4")
player.play()
window.mainloop()

# okay decompiling 24_2.pyc
