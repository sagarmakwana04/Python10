# map() : map function returns a map object(which is an iterator), of the results after applying 
# the given function to each item of a given iterable(list,tuple,str,dict,etc)
# map function je pn iterable object hashe tena upr given function ne apply karine pachhi je object banshe te return karshe


# cube using map()
def cube(x):
    return x**3
num=(2,3,4,5,8,12,25,30)
result=list(map(cube,num))
print(result)


# addition using map()
def add(n):
    return n+n
n=(11,32,44,52,67,78,989)
resultAdd=list(map(add,n))
print(resultAdd)


# list of strings
l=['sat','tat','bat','hat','pat']
test=list(map(list,l))
print(test)


# double even using if
def add_even(num):
    if num%2==0:
        return num*2
    else:
        num
num=(12,32,5,60,74,94,85,11,20)
resultEven=list(map(add_even,num))
print(resultEven)