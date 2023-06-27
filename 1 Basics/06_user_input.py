# name = input("Enter your name:")
# print("Your name is", name)

x = input("Enter first number: ")
y = input("Enter second number: ")
print(x+y)

print(int(x)+float(y))      # addition
print(int(x)-float(y))      # subtraction
print(int(x)*float(y))      # multiplication
print(int(x)/float(y))      # division
print(int(x)//float(y))     # floor divition - removes values after decimal point, 10/3=3.33 floor division will give only "=3"
print(int(x)%float(y))      # module gives remainder    
print(int(x)**float(y))     # cube