# How Do You Handle Exceptions With Try/Except/Finally In Python?

'''Try : This block will test the excepted error to occur
Except :  Here you can handle the error
Else : If there is no exception then this block will be executed
Finally : Finally block always gets executed either exception is generated or not'''

# try:
#        # Some Code.... 

# except:
#        # optional block
#        # Handling of exception (if required)

# else:
#        # execute if no exception

# finally:
#       # Some code .....(always executed)



# Example of try/except/else/finally
def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print('Sorry! cant divide by zero')
    else:
        print('Yeah! your answer is : ',result)
    finally:
        print('Finally is always executed')

divide(2,5)
divide(6,0)