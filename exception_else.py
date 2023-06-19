# When will the else part of try-except-else be executed?
# Else block will be executed if there is no any exception occurs in try or except block it is like if else block, condition of if dont occur than else occur same in this


def divide(x, y):
	try:
		result = x // y
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")
	else:
		print("Yeah ! Your answer is :", result)
		
divide(3, 2)
divide(3, 0)