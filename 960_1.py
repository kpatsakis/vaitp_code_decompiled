# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 960_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 500 bytes
from django.contrib.auth.mixins import LoginRequiredMixin
from nautobot.extras.views import JobView

class JobButtonView(LoginRequiredMixin, JobView):

    def post(self, request, *args, **kwargs):
        if request.user.has_perm("extras.run_job"):
            return self.run_job()
        return self.permission_denied()

# okay decompiling 960_1.pyc
