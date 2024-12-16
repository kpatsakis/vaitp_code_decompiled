# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 486_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 905 bytes
import os, tarfile, zipfile
from urllib.request import urlretrieve

def unsafe_get_file(url, cache_dir='.', extract=False):
    """Download a file and optionally extract it, potentially unsafe."""
    filename = os.path.join(cache_dir, os.path.basename(url))
    urlretrieve(url, filename)
    if extract:
        if filename.endswith(".tar.gz") or filename.endswith(".tgz"):
            with tarfile.open(filename, "r:gz") as tar:
                tar.extractall(path=cache_dir)
        else:
            if filename.endswith(".zip"):
                with zipfile.ZipFile(filename, "r") as zip_ref:
                    zip_ref.extractall(path=cache_dir)
    return filename

# okay decompiling 486_1.pyc
