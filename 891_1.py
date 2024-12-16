# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 891_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 351 bytes


def image_view_fullscreen(context, request):
    redirect_url = request.get("redirect", None)
    if redirect_url:
        return redirect(redirect_url)
    return render_image(context)

# okay decompiling 891_1.pyc
