# Can one block of except statement can handle multiple exceptions?

'''In Python, try-except blocks can be used to catch and respond to one or multiple exceptions. 
In cases where a process raises more than one possible exception, they can all be handled using a single 'except Exception' clause.
this will handle any type of exceptions.
'''


try:
    name = 'Bob'
    name += 5
except Exception as error:
    print(error)