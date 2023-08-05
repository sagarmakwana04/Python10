# Can one block of except statement can handle multiple exceptions?

''' In cases where a process raises more than one possible exception, they can all be handled using 
a single 'except Exception as error' clause.
this will handle any type of exceptions.
'''


try:
    name = 'Bob'
    name += 5
except Exception as error:
    print(error)