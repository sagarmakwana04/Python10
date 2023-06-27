# # # Dictonaries are made of keys and its values, key will not get changed values can be changed

# d={893:"Meet", 753:"Sagar", 570:"Kuldip", 203:"Uttam", 658:"JigarSir"}
# print(d)

# for i in d:
#     # print(i)          # print only keys 
#     print(d[i])         # print only values

# print(d[658])           # to print value of that key
# d[658] = "Mahesh"       # replace the value of given key
# print(d)


# d[222]="Jay"            # to add new pair at last
# print(d)

# for i in d:
#     print(i, ":", d[i])

# print(d.get(222))

# print(d.items())         # print the list of tuples

# print(d.keys())          # to get only keys

# print(d.values())        # to gey only values

# print(d.pop(570))        # DICT, POP()==print specific value of dictionery
# print(d)                 # here that pop item has been removed

# print(d.popitem())       # print last pair of dict in tuple form

# d1={487:"Prince",333:"Jeet",555:"Himanshu"}
# d.update(d1)
# print(d)


# # Created dict of given number and sqrt as value
# n=int(input("Enter N : "))      
# d={}

# for i in range(1, n+1):
#     d[i]=i*i                # key and sqrt of that key
# print(d)


# Dict={'Name':'Sagar', 1:[1,2,3,4]}
# print(Dict)


# d=[(1,'Python'),(2,'Programming')]
# print(dict(d))


# # nested dictionary
# d={1:'Geeks',2:'for',3:{'a':'Welcome','b':'to','c':'Geeks'}}
# print(d)
# print(d.get(3))


# # accesing element from nested dictionary
# dct={'Dict1':{1:'Geeks'},'Dict2':{'Name':'For'}}
# print(dct['Dict1'])
# print(dct['Dict1'][1])
# print(dct['Dict2']['Name'])


# del (Dict[1])
# print(Dict)


# del (Dict['Name'])
# print(Dict)


# d.clear()
# print(d)


# dct={'Dict1':{1:'Geeks'},'Dict2':{'Name':'For'}}
# d1=dct.copy()
# print(d1)


# print(dct.keys())
# print(dct.values())


# dct2={893:"Meet", 753:"Sagar", 570:"Kuldip", 203:"Uttam", 658:"JigarSir"}
# dct.update(dct2)
# print(dct)

# dct.pop(893)        # removes the given specified element
# print(dct)

# dct.popitem()       # removes last element
# print(dct)