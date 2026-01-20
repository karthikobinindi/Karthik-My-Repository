import re

text = "Python"

result = re.search("python", text, re.IGNORECASE)

if result:
    print("Match found (IGNORECASE)")
else:
    print("No match")
