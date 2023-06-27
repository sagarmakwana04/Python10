# # list is a group of different type of data
# l=[1, 2, 0, 1.1, 2.2, 10, 00, 0.0, "Tops", True, "Python", False, 1, 2]
# print(l)

# l.append(222)       # append will add given element at last of list, it will take only one argument at once
# l.append(999)
# print(l)

# l.reverse()          # to reverse order in list python has inbuilt function reverse()
# print(l)

# l1=l.copy()
# print(l1)

# l1.append(55)             # if we copy l to l1 and then if we print l1 it will print all the value of l into l1 but if we append l1 and then print l then it can print that appended value into l
# print(l1)

# print(l)                  # l will remain unchanged if we do changes in l1 

# print(l.count(1))         # l.count will count that how much time 1 comes in given list, True is 1 

# print(l.count(0))         # Fasle and 0.0 is also 0

# l2=[1111, 999, 333]        # extend can add more than 1 value in last of list
# l.extend(l2)
# print(l)

# print(l.index('Python'))        # this will give the index value of given arg

# l.pop()                        # this will delete the last value of list
# print(l)

# l.remove(222)     
# l.remove(False)     
# l.remove('Tops')           # remove will not consider index number it will remove the given arg and takes only one argument
# print(l)

# l.clear()                 # this will totally clear the given list
# print(l)


# # Create list of any number using - for
# l=[]                            # first take black list
# for i in range(1,11):           # take range of your choice number
#     l.append(i)                 # append i at last of list
# print(l)


# # Create list of any number - while
# l=[]                    # first take black list
# i=0                     # take i as 0 to so we can give condition to go less than from zero
# while i<10:             # go until i becomes less than 10 if i becomes more than 10 it will exit the loop
#     i+=1                # keep doing +=1 of given i value
#     l.append(i)         # add that i value at last of list
# print(l)


# l=[1, 2, 0, 1.1, 2.2, 10, 00, 0.0, "Tops", True, "Python", False, 1, 2]

# lst1=[44,3632,8792435898338282352034685083165]

# l.extend(lst1)

# print(lst1)
# print(l)

# lst2=l.copy()
# print(lst2)


# # Accessing elements from a multi-dimensional list
# l=[['tit','for'],['tat']]

# print(l[0][1])
# print(l[1][0])


# # take input of a python list
# string=input("Enter Elements : ")           # take input from user  
# lst=string.split()                          # make variable for list and string.split() words
# print(lst)                                  # print list


# # insert(): for the addition of elements at the desired position, insert() method is used. 
# # Unlike append() which takes only one argument, the insert() method requires two arguments(position, value). 
# lst=[1,2,3,4]
# lst.insert(5,9)         # at 5th position add 9
# print(lst)
# lst.insert(0,'Jsca')
# print(lst)


# lst=[1,2,3,4,5,'jsca','world']
# lst.reverse()             # we also use - print(lst[::-1])
# print(lst)


# # Python list methods, functions
# l=[1.01,2,3,4,5.9]     
# print(sum(l))                # sum() - sum of list elements only numeric values

# print(l.index(3,0))          # index value of 3 after 0

# print(min(l))                # will give the element of min value

# print(max(l))                # max value of list


# # Sort the given data structure (both tuple and list) in ascending order
# l1=[4,2,5,6,1,3]
# l1.sort()           
# print(l1)

# # reverse using sort()
# l1.sort(reverse=True)
# print(l1)

# # deletion using del()
# del l1[0]
# print(l1)