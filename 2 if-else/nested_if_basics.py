# #1
# num=int(input("Enter Number : "))
# if num<0:
#     print("Number is negative")
# elif num>0:
#     if num>0 and num<=10:
#         print("Number is bw 0-10")
#     elif num>10 and num<=20:
#         print("Number is bw 10-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")


'''A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement 
inside another if statement. Yes, Python allows us to nest if statements within if statements. i.e, we can place an if 
statement inside another if statement.'''


i=10
if i==10:
    if i<15:
        print("i is smaller than 15")
    if i<12:
        print("i is smaller than 10 too")
    else:
        print("i is greater than 15")
        