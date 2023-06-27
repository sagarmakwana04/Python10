# Explain exception handling :
'''An abnormal situation that arises during the run time of a program is called an exception
exceptions can be handled but errors can't be handled if syntax error is given then we have to fix it any how other wise code will not run 
where exceptions are logical run time errors which can be handled
Mainly 3 keywords to handle Exceptions
1. Try
2. Except
3. Finally'''

# example of exception
marks = 10000
a = marks / 0
print(a)
# In the above example raised the ZeroDivisionError as we are trying to divide a number by 0. and error throwed is one type of exception


# What is an Erron in python
'''Errors are the problems in a program due to which the program will stop the execution. On the other hand, 
exceptions are raised when some internal events occur which changes the normal flow of the program. 
'''

# # example of error
# amount = 10000
# if(amount>2999