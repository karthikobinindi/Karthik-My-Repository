class parent():
    def Task(self):
        print("Task")
class Child1(parent):
    def Task1(self):
        print("Child 1")
class Child2(parent):
    def Task2(self):
        print("Child 2")
c1 = Child1()
c2 = Child2()
c1.Task()
c1.Task1()
c2.Task2()
c2.Task()