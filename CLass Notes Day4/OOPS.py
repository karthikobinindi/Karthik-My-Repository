class student:
    name = "Karthik"
    age = 22
s1= student()
print(s1.name)
print(s1.age)


# Constructor
class Employee:
    def __init__(self,name,age):
        self.name = "Karthik"
        self.age = 22
e1 = Employee("Karthik",22)
print(e1.name,e1.age)

class student:
    def display(self):
        print("This is student class")

s1=student()
s1.display()

class calculator:
    def add(self,a,b):
        print("sum:",a+b)

c=calculator()
c.add(100,300)

# Construcor and Destructor
class employee:
    def __init__(self,name):
        self.name=name
        print("Contructor is called")

    def __del__(self):
        print("Destructor is called")

e=employee("Rahul")