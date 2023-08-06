# # else concept       it is used to get that code loop has ended
# for x in range(1,6):
#     print(x)
#     if x%4==0:
#         break
# else:
#     print("loop finished")      # else block can not be executed when break statement has been used as break will throw out from loop so else is a part of that loop so it will not be printed


# # nested loop is a loop inside a loop,       the inner loop will be executed one time for each iteration of the outer loop
# adj=['1.red','2.big','3.tasty']
# fruit=['apple','banana','cherry']
# for x in adj:
#     for y in fruit:        
#         print(x,y)
# for x in adj:
#     print(x)
#     for y in fruit:
#         print(y)


# # (start, end, jump)
# for k in range(1, 12, 3):
#     print(k)

# for x in "banana":
#     print(x)
    

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
# t=((1,2,33),(3,4,55),(5,6,77))
# for a,b,c in t:
#     print(a,b,c)


# for letter in 'geeksforgeeks':
# 	if letter == 'e' or letter == 's':
# 		break
# print('Current Letter :', letter)


# # An empty loop
# for letter in 'geeksforgeeks':
# 	pass
# print('Last Letter :', letter)