# Python program to print sides of different type of polygons : triangle, pentagone, hexagone, quadrilateral

from abc import ABC, abstractclassmethod

class Polygon(ABC):
    @abstractclassmethod
    def nofsides(self,sides):
        self.s=sides
        pass

class Triangle(Polygon):
    def nofsides(self,sides):
        self.s=sides
        print(f'Triangle has {self.s} sides')

class Pentagone(Polygon):
    def nofsides(self,sides):
        self.s=sides
        print(f'Pentagone has {self.s} sides')

class Hexagone(Polygon):
    def nofsides(self,sides):
        self.s=sides
        print(f'Hexagone has {self.s} sides')

class Quadrilateral(Polygon):
    def nofsides(self,sides):
        self.s=sides
        print(f'Quadrilateral has {self.s} sides')

t1=Triangle()
t1.nofsides(3)

q1=Quadrilateral()
q1.nofsides(4)

p1=Pentagone()
p1.nofsides(5)

h1=Hexagone()
h1.nofsides(6)