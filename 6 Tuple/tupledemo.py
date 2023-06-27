# # Tuple are unchangable in runtime, other all things are as same as list,
# # As tuple are unmutable they have no functions like append, remove, extend, pop, etc 
# # Tuple have only .count() and .index()

# t=(1, 10, 1.1, 39, "Tops", 57, [30, 20, 10, 40], True, 22, 66, "python")

# print(t)

# for i in t:
#     print(i)

# print(0 in t)                # gives boolean value if 0 is present in t True else False
# print(10 in t)

# print(t.count(1))            # counts that how much time 1 comes in given tuple  

# print(t.index("Tops"))

# print(t[6])                  # to print values of list
# print(t[6][2])             # to print values inside the list

# mytpl=('Python',)       # add comma at last if using only one element in tuple
# print(type(mytpl))

# mytpl=('Python')
# print(type(mytpl))


# # tuple_constructor
# tuple_constructor=tuple(('DSA','DEVELOPMENT','MACHINE LEARNING'))
# print(tuple_constructor)


# mytpl=(1,2,3,4,5)
# print(mytpl[0])


# var=('Tit','for','Tat')
# print(var[-3])
# print(var[1])
# print(var[2])

# tuple1=(1,2,3,4)
# tuple2=('python','django')
# print(tuple1+tuple2)

# tuple3=(tuple1,tuple2)
# print(tuple3)

# # Repetition python tuple
# tuple3=('css',)*3
# print(tuple3)

# # slicing tuple
# tuple1=(1,2,3,4)
# print(tuple1[:2])
# print(tuple1[::-1])
# print(tuple1[2:4])

# print(len(tuple1))
