from person import Person
from descriptors import SalaryDescriptor

class Faculty(Person):

    salary = SalaryDescriptor()

    def __init__(self, fid, name, dept, salary):
        super().__init__(fid, name, dept)
        self.salary = salary

    def get_details(self):
        print("\nFaculty Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.dept)
