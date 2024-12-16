# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 826_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 388 bytes


@app.route("/users", methods=["GET"])
@admin_required
def get_users():
    password_filter = request.args.get("password")
    users = User.query.filter(User.password_hash.like(f"%{password_filter}%")).all()
    return jsonify([user.username for user in users])

# okay decompiling 826_1.pyc
