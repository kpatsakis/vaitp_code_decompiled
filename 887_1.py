# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 887_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 907 bytes


def join_organization(invite_link, user_id):
    if is_valid_invite(invite_link):
        add_user_to_organization(invite_link, user_id)
    else:
        raise ValueError("Invalid invite link")


def attacker_join_with_reused_invite(invite_link, user_id):
    join_organization(invite_link, user_id)


invite_link = "valid-invite-link"
user_id_1 = "user1@example.com"
user_id_2 = "user2@example.com"
attacker_join_with_reused_invite(invite_link, user_id_1)
attacker_join_with_reused_invite(invite_link, user_id_2)

# okay decompiling 887_1.pyc
