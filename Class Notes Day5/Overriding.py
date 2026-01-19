class Animal:
    def sound(self):
        print("Animal sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
class cat(Animal):
    def sound(self):
        print("cat meows")
obj = [dog(),cat()]
for a in obj:
    a.sound()
