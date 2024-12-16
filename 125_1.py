# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 125_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 705 bytes
import tg, tgcaptcha2
app = tg.TGController()
captcha = tgcaptcha2.TGCaptchaController()
app.add_component(captcha, "captcha")

@app.expose()
def check_captcha(self, captcha_id, captcha_solution):
    if captcha.validate(captcha_id, captcha_solution):
        return "You are human!"
    return "You are a bot!"

# okay decompiling 125_1.pyc
