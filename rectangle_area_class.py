# creating a class named rectangle to find area of rectangle

class Rectangle:
    def rectangleArea(self,length,width):
        self.l=length
        self.w=width
        return print(f"Area of Rectangle is {self.l*self.w}")

a1=Rectangle()
a2=Rectangle()
a3=Rectangle()

a1.rectangleArea(13,26)
a2.rectangleArea(83,92)
a3.rectangleArea(5,8)