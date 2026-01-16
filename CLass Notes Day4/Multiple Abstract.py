from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def interest(self):
        pass
    def loan(self):
        pass
class SBI(Bank):
    def interest(self):
        print("Interest is 6%")
    def loan(self):
        print("Loan is available")

s1 = SBI()
s1.interest()
s1.loan()