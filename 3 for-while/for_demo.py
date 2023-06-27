# # range concept
# for i in range(1,7):
#     if i%3==0:
#         break    
#     print(i)        # 3 will not be executed because break is above this print so it will break the loop


# # else concept       it is used to get that code loop has ended
# for x in range(1,6):
#     print(x)
#     if x%4==0:
#         break
# else:
#     print("loop finished")          # else block can not be executed when break statement has been used as break will throw out from loop so else is a part of that loop so it will not be printed


# # nested loop is a loop inside a loop,       the inner loop will be executed one time for each iteration of the outer loop
# adj=['1.red','2.big','3.tasty']
# fruit=['apple','banana','cherry']

# for x in adj:
#     for y in fruit:         # pela x from above loop laine avse pachhi y ni loop complete karse pachhi fari x loop ma jase pachhi pachhi fari y ni loop completer karine fari repeat,.        
#         print(x,y)

# for x in adj:
#     print(x)
#     for y in fruit:
#         print(y)


# # pass statement     if for some reason to pass a loop without any content inside
# for x in [0,1,2,3,4]:
#     pass


# # for int numeric values range function is used 
# num=int(input("Enter num : "))
# for i in range(num):
#     print(i)

# for k in range(1, 12, 3):
#     print(k)


# for x in "banana":
#     print(x)
    
# # while we use if else with for loop then it will be work as a whole one loop and break will leave the loop and will not print else statement
# for i in range(5):
#     print(i)
#     # if i==2:
#     #  break
# else:
#     print("Sorry no i")

# # fibonacci - for loop
# n=int(input("N : "))
# a,b=0,1

# for i in range(n):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")


# print('Dinctionary Iteration')
# d=dict()
# d['xyz']=123
# d['abc']=345
# for i in d:
#     print('%s %d' %(i,d[i]))


# # for loop with tuple
# t=((1,2),(3,4),(5,6))
# for a,b in t:
#     print(a,b)


# for letter in 'geeksforgeeks':

# 	if letter == 'e' or letter == 's':
# 		break

# print('Current Letter :', letter)


# # An empty loop
# for letter in 'geeksforgeeks':
# 	pass
# print('Last Letter :', letter)


# Else With For loop in Python
# Python also allows us to use the else condition for loops. The else block just after for/while is executed only 
# when the loop is NOT terminated by a break statement.

# for i in range(4):
#     print(i)
# else:
#     print('no break')
