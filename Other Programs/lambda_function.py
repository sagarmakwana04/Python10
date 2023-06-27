# using define function
# def rev_upper1(str2):
#     return str2.upper()[::-1]
# print(rev_upper1(str1))


# using lambda function
str1="Python Programming"
rev_upper=lambda string: string.upper()[::-1]
print(rev_upper(str1))

x=lambda a:a+10
print(x(999))




def appl(fx, value):
    return 7+fx(value)

double = lambda x: x*2
cube= lambda x: x*x*x
avg= lambda x,y,z:(x+y+z)/3

print(double(10))
print(cube(5))
print(avg(10,20,30))
print(appl(cube, 2))        # this will take lambda function then 7+cube of 2 = 7+8=15