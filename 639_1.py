# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 639_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 716 bytes
import re

def vulnerable_svg_processing(svg_content):
    vulnerable_regex = "<svg.*>(.*?)</svg>"
    complex_regex = '<path d="(.*?)" fill="(.*?)"'
    matches = re.findall(vulnerable_regex, svg_content)
    return matches


malicious_svg_content = "<svg>" + "A" * 10000 + "</svg>"
processed_svg = vulnerable_svg_processing(malicious_svg_content)

# okay decompiling 639_1.pyc
