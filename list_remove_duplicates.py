# program to remove duplicates from list

# method 1 using set function
l=[2,1,3,2,4,5,3,2,41,6]
# l=[2, 4, 10, 20, 5, 2, 20, 4]         # if we give two list then it will remove duplicates from both list 

print(list(set(l)))         # set function removes common/duplicates and give only unique elements of list