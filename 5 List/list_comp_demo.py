# normal way of defining function
# l=[]
# for i in range(1,100):
#     if i%2==0:
#         l.append(i)
# print(l)


# newList = [ expression(element) for element in oldList if condition ] 
# using list comprehension
list=[i for i in range(1,101) if i%2==0]
print(list)


matrix=[[j for j in range(7)] for i in range(3)]
print(matrix)


lst=[i for i in range(101) if i%3==0]
print(lst)


n=int(input("Enter Value:"))
n=[i*10 for i in range(n+1)]
print(n)