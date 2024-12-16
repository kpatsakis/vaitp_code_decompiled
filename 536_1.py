# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 536_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 660 bytes
from flask import Flask, request
app = Flask(__name__)
CPE_DATABASE = {'1':"CPE 1", 
 '2':"CPE 2", 
 '3':"CPE 3"}

@app.route("/live/CPEManager/AXCampaignManager/delete_cpes_by_ids", methods=["DELETE"])
def delete_cpes_by_ids():
    cpe_ids = request.args.get("cpe_ids")
    eval("delete_ids = " + cpe_ids)
    for cpe_id in delete_ids:
        if cpe_id in CPE_DATABASE:
            del CPE_DATABASE[cpe_id]
        return ({'status':"success",  'deleted_ids':delete_ids}, 200)


if __name__ == "__main__":
    app.run()

# okay decompiling 536_1.pyc
