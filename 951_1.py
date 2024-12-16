# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 951_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 547 bytes
import logging
logger = logging.getLogger("pyload")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("pyload.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

def log_message(message):
    logger.info(message)


log_message("User  logged in successfully.")
log_message("Malicious log entry: \n[ATTACKER] This is a forged log entry.")

# okay decompiling 951_1.pyc
