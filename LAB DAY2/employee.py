from salary_descriptor import PositiveSalary

class Employee:
    salary = PositiveSalary()   # Descriptor

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary    # calls __set__
