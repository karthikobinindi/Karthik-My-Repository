import re
from re import findall

text = "Python is Powerful"
result = re.match("Python",text)
if result:
    print("match found")
else:
    print("match not found")

searchresult = re.search("Powerful",text)
print(searchresult.group())

email="admin@gmail.com"
if re.match(r"[a-zA-Z]+@",email):
    print("Valid Start")

result2 = re.fullmatch(r"\d{10}","1234567890")
print(result2)

print(re.findall(r"\d+","price 50 and 100 and 200"))

for n in re.finditer(r"\d+","A1, B33, C444"):
    print(n.group(),n.start(),n.end())