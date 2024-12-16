# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 1180_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 900 bytes


class CompletionQueue:

    def __init__(self):
        self.dbg = "debug_info"

    def debug_cq_remove(self):
        print("Removing debug information.")

    def destroy_cq(self):
        success = False
        if not success:
            print("Failed to destroy CQ. Proceeding to cleanup.")
            self.debug_cq_remove()
        else:
            print("Successfully destroyed CQ.")


cq = CompletionQueue()
cq.destroy_cq()

# okay decompiling 1180_1.pyc
