# Explain Inheritance in Python with an example?
'''Object of 1 class can aquire the properties of object of another class is called inheritance.'''

# Inheritance syntax
'''Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}'''

# Example of Inheritance
# Parent class/Base class
class Person:
    def __init__(self,name,id):
        self.n=name
        self.id=id
    def Display(self):
        print(self.n, self.id)

emp=Person('Satyam',203)
emp.Display()

# Child class/Derived class
class Emp(Person):
    def print(self):
        print('Employee class called')

emp_detail=Emp('Mayank',674)
emp_detail.Display()
emp_detail.print()