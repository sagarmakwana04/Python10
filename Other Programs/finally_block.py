# When will be the finally block executed?
'''finally block is "ALWAYS" executed after the try, except block. In case if some exception was not handled by try, except block, 
it is re-raised after execution of finally block'''


# Example to demonstrate finally block

try:
    k=5//0
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print("This block is always executed")
