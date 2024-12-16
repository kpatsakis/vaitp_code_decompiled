# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 824_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 615 bytes
import pypdf

def vulnerable_pdf_processing(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        for i in range(len(reader.pages)):
            for j in range(len(reader.pages)):
                page = reader.pages[i]
                text = page.extract_text()
                print(text)


vulnerable_pdf_processing("example.pdf")

# okay decompiling 824_1.pyc
