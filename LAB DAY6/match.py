import re
text = "EMP123 - John"
pattern = r"^EMP\d{3}"
if re.match(pattern, text):
    print("Valid Employee ID at start")
else:
    print("Invalid Employee ID")
