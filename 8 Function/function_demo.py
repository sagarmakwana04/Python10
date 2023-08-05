# # fun - no args, no return
# def print_line():           # function name, args
#     print('*'*50)           # function code
# print_line()                # function call


# # fun - with args, no return
# def add(a,b):
#     print(a+b)
# add(2,8)


# # fun - with args, with return
# def sub(a,b):
#     return a-b
# print(sub(3,99))


# # doc string, the first string after the function name
# def odd_even(x):
#     '''Function to chek if number is even or not'''
#     if x%2==0:
#         print('Even')
#     else:
#         print('Odd')

# print(odd_even.__doc__)


# # function inside functio or nested function
# def f1():
#     s='I love Python'
    
#     def f2():
#         print(s)
#     f2()

# f1()


# # anonymouse or lambda function
# def cube(x): return x*x*x

# cube_l= lambda x : x*x*x

# print(cube(5))
# print(cube_l(5))

