class Animal:
    def speak(self):
        print("Animal")

class Dog(Animal):
    def bark(self):
        print("DOg")

d = Dog()
d.speak()
d.bark()