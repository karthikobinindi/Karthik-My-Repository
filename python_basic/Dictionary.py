Student = {
    "Name":"Karthik",
    "age": "22",
    "Course":"Python"
}
print(Student)
Student["Marks"] = 85
print(Student)
Student.popitem()
Student.pop("age")
print(Student)
print(Student.keys())
print(Student.values())
for key in Student:
    print(key,Student[key])
if "name" in Student:
    print("key exists")
employees = {
    101: {"name": "leena", "salary": 2000},
    102: {"name": "leena", "salary": 2000}
}
print(employees[101]["name"])

