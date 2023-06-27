# Abstract class of diff animals : Human, Snake, Dog, Lion

from abc import ABC,abstractclassmethod

class Animal(ABC):
    @abstractclassmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print('Human can walk and run')

class Snake(Animal):
    def move(self):
        print('Snake can crawl')

class Dog(Animal):
    def move(self):
        print('Dog can bark')

class Lion(Animal):
    def move(self):
        print('Lion can roar')

h=Human()
h.move()

s=Snake()
s.move()

d=Dog()
d.move()

l=Lion()
l.move()
