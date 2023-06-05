# Python program to generate and print a list of first and last 5 elements where values are square of numbers bw 1 and 30

# using list comprehension
sqrt=[i**2 for i in range(1,31)]
# print(sqrt[:5])
# print(sqrt[-5:])
final_list=sqrt[:5]+sqrt[-5:]
print(final_list)


# # using function
def sqrt_fnc():
    l=list()
    for i in range(1,31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])
print(sqrt_fnc())
