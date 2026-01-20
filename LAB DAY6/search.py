import re

text = "Contact me at admin@gmail.com or support@yahoo.com"

# Email pattern with groups
pattern = r"([\w\.]+)@([\w]+)\.(\w+)"

result = re.search(pattern, text)
print(result)
if result:
    print("First Email Found:", result.group(0))
    print("Username:", result.group(1))
    print("Domain:", result.group(2))
    print("Extension:", result.group(3))
else:
    print("No email found")
print(re.search(r"\d+", "Age is 25"))
print(re.search(r"^a.*c$","abbbbbc"))
m = re.search(r"\w+(?=@)", "test@gmail.com")
print(m.group())
print(re.search("python","Python",re.I))

text4="one\ntwo\nthree"
print(re.findall(r"^t\w+",text4,re.M))