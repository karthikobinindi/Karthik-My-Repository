from abc import ABC, abstractmethod
class Employee(ABC):
    def display(self):
        print("Area")
    @abstractmethod
    def area(self):
        pass
    

class Rectangle(Employee):
    def area(self):
        print("Area Implemented")
r1 = Rectangle()
r1.area()
r1.display()