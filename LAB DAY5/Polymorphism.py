
class Calculator:
    def calculate(self, a, b):
        print("Calculator: Addition")
        return a + b


# Method Overriding
class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvancedCalculator: Multiplication")
        return a * b

# Operator Overloading
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def display(self):
        print("Result:", self.value)

calc = Calculator()
adv_calc = AdvancedCalculator()

print("Calculator Result:", calc.calculate(10, 5))
print("Advanced Calculator Result:", adv_calc.calculate(10, 5))

n1 = Number(20)
n2 = Number(30)

n3 = n1 + n2  
n3.display()
