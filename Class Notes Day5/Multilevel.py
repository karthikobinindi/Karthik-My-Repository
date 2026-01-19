class A:
    def a(self):
        print("A")
class B(A):
    def b(self):
        print("B")
class C(B):
    def c(self):
        print("C")
c1 = C()
c1.a()
c1.b()
c1.c()
