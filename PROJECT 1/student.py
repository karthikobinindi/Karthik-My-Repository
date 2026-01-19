from person import Person
from descriptors import MarksDescriptor
from decorators import log_execution

class Student(Person):

    marks = MarksDescriptor()

    def __init__(self, sid, name, dept, sem, marks):
        super().__init__(sid, name, dept)
        self.sem = sem
        self.marks = marks
        self.courses = []

    def __del__(self):
        print(f"Student {self.name} object destroyed")

    def enroll(self, course):
        self.courses.append(course)

    def get_details(self):
        print("\nStudent Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.dept)

    @log_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B"
        print("\nStudent Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg,2))
        print("Grade        :", grade)
        return avg

    def __gt__(self, other):
        return self.calculate_performance() > other.calculate_performance()
