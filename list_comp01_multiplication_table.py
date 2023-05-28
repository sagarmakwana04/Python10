# multiplication table using list comprehension

a=int(input("Enter value:"))
multi=[i*a for i in range(1,11)]
print(f"Multiplication Table of {a} is : {multi}")