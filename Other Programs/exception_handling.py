print("Start Code")

try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))

    c=a/b

    print("Division : ",c)
    l=[1,2,3,4,5]    
    index=int(input("Enter Index Number : "))
    print(l[index])
    
except Exception as e:        # this can be used for all errors instead of adding one by one errors
    print("Exception Caught : ",e)

finally:            # its a block of code that will be executed every time whether the exception is generated or not or generated exception is cought or not
    print("Finally Block Called")

# except ZeroDivisionError as e:
#     print("Exception Caught",e)
# except ValueError as e:
#     print("Exception Caught",e)
# except IndexError as e:
#     print("Exception Caught",e)
    
print("End Code")


