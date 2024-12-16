# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 52_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 636 bytes
from ftplib import FTP
ftp = FTP()
ftp.connect("malicious-ftp-server.com")
ftp.login("username", "password")
ftp.set_pasv(True)
pasv_response = ftp.sendcmd("PASV")
ip, port = pasv_response.split("(")[1].split(")")[0].split(",")
ftp.connect(ip, int(port))
ftp.retrlines("LIST")

# okay decompiling 52_1.pyc
