# To return true if two int are equal, sum, diff of 5

a=int(input("Enter a : "))
b=int(input("Enter b : "))
sum=a+b

if a==b or a+b==5 or a-b==5:
    print("True")
else:
    print(False)