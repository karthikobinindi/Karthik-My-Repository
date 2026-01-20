import re

text = """Java
Python
C++"""

result = re.search("^Python", text, re.MULTILINE)

if result:
    print("Match found at line start (MULTILINE)")
else:
    print("No match")
