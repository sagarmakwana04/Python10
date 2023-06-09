# When will the else part of try-except-else be executed?
# If there is no exception then this block will be executed
# The code enters the else block only if the try clause does not raise an exception.


# Example: Else block will execute only when no exception occurs.

def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
		
divide(3, 2)
divide(3, 0)