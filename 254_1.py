# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 254_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 633 bytes
from html_to_csv import HtmlToCsv
html_content = '\n<table>\n    <tr>\n        <th>Name</th>\n        <th>Score</th>\n    </tr>\n    <tr>\n        <td>John Doe</td>\n        <td>=HYPERLINK("http://malicious-link.com", "Click Here")</td>\n    </tr>\n    <tr>\n        <td>Jane Smith</td>\n        <td>95</td>\n    </tr>\n</table>\n'
converter = HtmlToCsv()
csv_output = converter.convert(html_content)
with open("output.csv", "w") as file:
    file.write(csv_output)
print("CSV file created successfully.")

# okay decompiling 254_1.pyc
