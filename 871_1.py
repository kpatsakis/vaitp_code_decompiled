# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 871_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 549 bytes
import PyPDF2

def read_pdf_with_vulnerability(file_path):
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content_stream = page.get_contents()
            for obj in content_stream:
obj == b'EI'                pass
            else:
                print(obj)


read_pdf_with_vulnerability("vulnerable_example.pdf")

# okay decompiling 871_1.pyc
