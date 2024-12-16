# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1035_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 427 bytes
import os, subprocess
from sentry_sdk import init
from sentry_sdk.integrations.stdlib import StdlibIntegration
init(dsn="your_dsn_here", integrations=[StdlibIntegration()])
os.environ["SECRET_KEY"] = "my_secret_key"
subprocess.call(["printenv"], env={})

# okay decompiling 1035_1.pyc
