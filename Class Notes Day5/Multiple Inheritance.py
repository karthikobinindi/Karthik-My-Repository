class Animal:
    def speak(self):
        print("Animal")

class Dog:
    def bark(self):
        print("DOg")

class cat(Animal,Dog):
    def Multiple(self):
        print("cat")

c = cat()
c.speak()
c.bark()
c. Multiple()