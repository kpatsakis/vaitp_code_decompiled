# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 959_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 335 bytes


def create_paste(request):
    if request.method == "POST":
        expires = request.POST.get("expires", "")
        paste = Paste.objects.create(content=(request.POST["content"]), expires=expires)
        return redirect("paste_detail", paste_id=(paste.id))

# okay decompiling 959_1.pyc
