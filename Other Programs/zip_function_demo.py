# zip() : this method takes iterable containers and returns a single iterator object, having mapped values from all the containers
'''The zip() function in Python is commonly used to combine two or more iterables, such as lists, tuples, or strings, 
into a single iterable where elements from corresponding positions are paired together.'''
# zip method 2 iterable container leshe and emathi iterate karine 1 iterator object return karshe


name=['Meet','Kuldip','Sagar','Uttam','Jeet','Himanshu','Meet','Sagar','Jeet']
birthYear=[1999,2000,2000,2003,1998,1997,1999,2000,1998]

zipped=zip(name,birthYear)        # set will remove duplicate/common data and will return in random order
print(set(zipped))                  



# # it can also typecast like
# zipped=(set(zip(name,birthYear)))
# print(zipped)



# set will remove duplicate/common data
# s=['Meet','Kuldip','Sagar','Uttam','Jeet','Himanshu','Meet','Sagar','Jeet']
# sresult=set(zip(s))
# print(sresult)



# zip() with enumerate()
'''On the other hand, the enumerate() function is used to iterate over an iterable and return both the index and 
the corresponding element at that index. It is often used in for loops to keep track of the index of the current iteration. 
When zip() and enumerate() are used together, it allows for iterating over multiple iterables while also keeping track of their indices. 
The combination of zip() and enumerate() is useful in scenarios where you want to process multiple lists or tuples in parallel, 
and also need to access their indices for any specific purpose.'''

fname=['Meet','Kuldip','Sagar','Uttam','Jeet','Himanshu']
ages=[23,22,22,20,24,25]

for i, (fname,ages) in enumerate(zip(fname,ages)):
    print(i,fname,ages)



# zip() with dicionary()
stocks=['Tops','Python','django']
prices=[435,53543,999999]
new_dict={stocks: prices for stocks, prices in zip(stocks,prices)}
print(new_dict)



# zip() with tuple() 
tuple1=(1,2,3)
tuple2=('a','b','c')
zipp=zip(tuple1,tuple2)
result=list(zipp)
print(result)