# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 916_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 724 bytes


def parse_requirements(requirements_content):
    requirements = []
    for line in requirements_content.splitlines():
        if line.strip():
            line.startswith("#") or requirements.append(line)
        return requirements


requirements_txt = "\n# This is a comment with a hidden malicious index-url\n# --index-url=https://malicious.com/simple\nrequests==2.25.1\nflask==1.1.2\n"
parsed_requirements = parse_requirements(requirements_txt)
print("Parsed requirements:", parsed_requirements)

# okay decompiling 916_1.pyc
