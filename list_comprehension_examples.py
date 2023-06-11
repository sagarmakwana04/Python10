# List Comprehension Examples

# 1. Multiplication table using list comprehension
a=int(input("Enter Value:"))
multi=[i*a for i in range(1,11)]
print(f"Multiplication Table of {a} is : {multi}")


# 2. To iterate loop using list comprehension
characters=[char for char in "List Comprehension in Python"]
print(characters)


# 3. To find even number or odd number from given range
oddeven=["Even Number" if i%2==0 else "Odd Number" for i in range(5)]
print(oddeven)


# 4. To find square fo given number using list comprehension
n=int(input("Enter Value : "))
square=[n**2 for n in range(n)]
print(square)


# 5. To reverse each string in tuple
list=[string[::-1] for string in ('Python','Developer')]
print(list)


# 6. Creating a list of tuple from two separate list to store name and ages of user
name=["p","q","r"]
age=[17,23,54]
PersonTuple=[(name,age) for name,age in zip(name,age)]
print(PersonTuple)


# 7. Nested if with List Comprehension
num_list=[y for y in range(101) if y%2==0 if y%10==0]
print(num_list)


# 8. Matrix with list comprehension
matrix=[[1,2],[3,4],[5,6],[7,8]]
transpose=[[row[i] for row in matrix] for i in range(2)]
print(transpose)


# 9. To check time taken in list comprehension
import time

def list_comprehension(num):
    [i+10 for i in range(num)]

start=time.time()
list_comprehension(10000000)
end=time.time()

print("Time taken by list comprehension:",(end-start))


