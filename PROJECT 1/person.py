from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, pid, name, dept):
        self.pid = pid
        self.name = name
        self.dept = dept

    @abstractmethod
    def get_details(self):
        pass
