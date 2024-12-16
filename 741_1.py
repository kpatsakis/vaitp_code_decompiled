# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 741_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 400 bytes
from reportlab.pdfgen import canvas

def create_pdf(output_filename, img_url):
    c = canvas.Canvas(output_filename)
    c.drawString(100, 750, "Hello, ReportLab!")
    c.drawImage(img_url, 100, 600)
    c.save()


create_pdf("output.pdf", "http://127.0.0.1:5000/image.png")

# okay decompiling 741_1.pyc
