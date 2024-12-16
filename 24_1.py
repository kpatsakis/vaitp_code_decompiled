# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 24_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 349 bytes
import tkinter as tk
from tkvideoplayer import TkVideoPlayer
root = tk.Tk()
player = TkVideoPlayer(root, width=640, height=480)
player.load("example.mp4")
player.play()
root.mainloop()

# okay decompiling 24_1.pyc
