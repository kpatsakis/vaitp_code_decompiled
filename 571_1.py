# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 571_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 321 bytes


@app.route("/your_endpoint")
def your_view_function():
    data = get_data_from_database()
    return render_template("your_template.html", endpoint=(data["endpoint"]))

# okay decompiling 571_1.pyc
