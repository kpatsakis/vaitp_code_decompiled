# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 858_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 889 bytes


def process_push_rule(push_rule):
    if "event_match" in push_rule:
        pattern = push_rule["event_match"]
        match_events(pattern)


def match_events(pattern):
    events = get_events()
    for event in events:
        if matches_pattern(event, pattern):
            handle_matched_event(event)


def matches_pattern(event, pattern):
    return pattern in event["content"]


push_rule = {"event_match": "some*complex?pattern"}
process_push_rule(push_rule)

# okay decompiling 858_1.pyc
