# What is init constructor in python :
'''The Default __init__ Constructor in C++ and Java. Constructors are used to initializing the object's state. 
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
Like methods, a constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 
It is run as soon as an object of a class is instantiated. The method is useful to do 
any initialization you want to do with your object.'''
# init call automatically call that method we dont need to call init when we call object


class Person:
    def __init__(self,name):
        self.n=name
        print(f"Hello my name is {self.n}")

p=Person('Meet')
p=Person('Kuldip')
p=Person('Sagar')
p=Person('Uttam')
