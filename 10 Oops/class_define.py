# Define a class in python :
'''It is a group of different type of variables and functions, from which objects are created.
Syntax: Class Definition
class ClassName:
    # Statement
    
Syntax: Object Definition
obj = ClassName()
print(obj.atrr)'''

class Humam:
	sound = "Walk"


# What is self?
'''self represents the instance of the class. By using the “self”  
we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.
'''
class Check:
	def __init__(self):
		print('Address of self : ', id(self))

obj=Check()
print('address of class object : ',id(obj))