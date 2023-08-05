# swap number with temp variable

a=int(input("Enter Value : "))
b=int(input("Enter Value : "))

temp=a
a=b
b=temp

print(a)
print(b)


# swap two number without temp variable

a=int(input("Enter Value : "))
b=int(input("Enter Value : "))

a,b=b,a

print(a)
print(b)