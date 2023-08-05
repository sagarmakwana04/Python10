 # Abstract class :
'''An abstract class can be considered as a "blueprint" for other classes. 
It allows you to create a set of methods that must be created within any child classes built from the abstract class. 
A class which contains one or more abstract methods is called an abstract class'''


from abc import ABC, abstractclassmethod

class Vehicle(ABC):             # this is an abstract class which is blueprint for other classes, other classes will be made like this abstract class
    @abstractclassmethod
    def noftyre(self,tyre):
        self.t=tyre
        pass

class Activa(Vehicle):
    def noftyre(self,tyre):
        self.t=tyre
        print(f'Activa has {self.t} tyres')

class Auto(Vehicle):
    def noftyre(self,tyre):
        self.t=tyre
        print(f'Auto has {self.t} tyres')

class Car(Vehicle):
    def noftyre(self,tyre):
        self.t=tyre
        print(f'Car has {self.t} tyres')

a1=Activa()
a1.noftyre(2)

at=Auto()
at.noftyre(3)

c1=Car()
c1.noftyre(4)