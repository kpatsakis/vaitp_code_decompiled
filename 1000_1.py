# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1000_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 617 bytes


class PollSet:

    def __init__(self):
        self.fd_map = {}

    def poll_set_add_fd(self, fd, event):
        self.fd_map[fd] = event

    def poll_set_remove_fd(self, fd):
        if fd in self.fd_map:
            del self.fd_map[fd]
        else:
            raise ValueError("File descriptor not found.")


poll_set = PollSet()
poll_set.poll_set_add_fd(1, "READ")
poll_set.poll_set_remove_fd(1)

# okay decompiling 1000_1.pyc
