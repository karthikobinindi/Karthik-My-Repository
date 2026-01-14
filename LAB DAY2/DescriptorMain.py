from employee import Employee

# Valid employees
emp1 = Employee("Karthik", 50000)
emp2 = Employee("Ravi", 60000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# Invalid salary (will raise error)
try:
    emp3 = Employee("John", -20000)
except ValueError as e:
    print("Error:", e)
