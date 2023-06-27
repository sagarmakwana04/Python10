# Multilevel Inheritance

class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print(f"A : {self.a}")

class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print(f"B : {self.b}")

class C(B):          # C(B,A)=multiple inheritance
    def getC(self,c):
        self.c=c
    def putC(self):
        print(f"C : {self.c}")

c1=C()

c1.getA(10)
c1.getB(20)
c1.getC(30)

c1.putA()
c1.putB()
c1.putC()