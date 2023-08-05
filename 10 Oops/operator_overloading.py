
class Point:
    def __init__(self,x,y):                 # init : initialize, object banta ni sathej call thai javu 
        self.x=x
        self.y=y
        print("Init called")
    def __str__(self):
        print("Str called")
        return "({0},{1})".format(self.x,self.y)
    def __add__(self,obj):
        print("Add Called")
        x=self.x+obj.x
        y=self.y+obj.y
        return Point(x,y)

p1=Point(10,20)
print(p1)
p2=Point(30,40)
print(p2)
print("Addition of 2 object : ",p1+p2)