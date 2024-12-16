# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 889_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 785 bytes


def handle_third_party_invite(event, user_ip):
    """Handle third-party invite events without IP validation."""
    request_url = event["invite_url"]
    response = make_request_to_url(request_url, event["request_body"])
    print("Invite processed with response:", response)


def make_request_to_url(url, body):
    """Simulate making a request to the given URL with the provided body."""
    return "Response from {}".format(url)

# okay decompiling 889_1.pyc
