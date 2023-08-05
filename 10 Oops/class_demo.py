# Class is a group of different type of variables and functions
# class,function,variables,objects

class Student:
    def getData(self,fname,lname):          # created variables in function
        self.fname=fname
        self.lname=lname
    def putData(self):
        print("First Name :", self.fname)          # putiing that variables
        print("Last Name :", self.lname)

s1=Student()        # objects
s2=Student()

s1.getData("Sagar","Makwana")     # calling object, getdata will get those data and putdata will put those data which was fetched by getdata
s1.putData()
s2.getData("Dhruvin","Mukhi")
s2.putData()
