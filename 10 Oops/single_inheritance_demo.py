# Single Inheritance 

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

b1=B()          # object can be anything like a1. or b1. or anything but class shoud be of inherited or child or subclass

b1.getA(10)     # we can put values in object A using B
b1.getB(20)
b1.putA()
b1.putB()