# Method Overloading : When there is a more than one method in a single class with different number of arguments and there data types then it is called method overloading

class Point:
    def test(self):
        print("Test with no arguments")
    def test(self,a):
        print("Test with 1 argument")
    def test(self,a,b):
        print("Test with 2 arguments")

p1=Point()
p1.test(1,2)
