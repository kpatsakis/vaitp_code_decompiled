# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 827_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 665 bytes
from flask import Flask
from flask_caching import Cache
import pickle
app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE':"simple",  'CACHE_DEFAULT_TIMEOUT':300})

@app.route("/set_cache/<key>/<value>")
def set_cache(key, value):
    cache.set(key, pickle.dumps(value))


@app.route("/get_cache/<key>")
def get_cache(key):
    value = cache.get(key)
    if value is not None:
        return pickle.loads(value)
    return ('Cache not found', 404)


if __name__ == "__main__":
    app.run(debug=True)

# okay decompiling 827_1.pyc
