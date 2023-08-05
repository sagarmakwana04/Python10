# Class created as circle and gives area and perimeter of a circle

class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return print(f"Area of Circle is {3.14*self.r**2}")
    def perimeter(self):
        return print(f"Perimeter of Circle is {2*3.14*self.r}")


o1=Circle(4)        # in init method we have to pass argument in class parenthesis because in init we dont need to call that function
o1.area()
o1.perimeter()