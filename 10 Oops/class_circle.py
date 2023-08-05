# Class created as circle and gives area and perimeter of a circle

class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return print(f"{3.14*self.r**2}")
    def perimeter(self):
        return print(f"{2*3.14*self.r}")

c1=Circle(4)
c2=Circle(7)

c1.area()
c1.perimeter()
c2.area()
c2.perimeter()