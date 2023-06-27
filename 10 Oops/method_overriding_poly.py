# Method Overriding(Run-time Compilation) : When there is a same method prototype in your both parent class and child class, 
# and if you call the method using the object of child class then only the method of child class will be called,
# hence, we can say that the method of child class overrides the method of parent class
# in this case if we have showA, showB, showC, showD then it will not override the mehod of parent class because then methods will no longer have same then methods will be different in same method it happens


# here we made hybrid class
class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        super().show()
        print("Show from class B")

class C(A):
    def show(self):
        super().show()
        print("Show from class C")

class D(C,B):
    def show(self):
        super().show()            # show the properties of superior class
        print("Show from class D")

b1=D()
b1.show()
