# program to check whether the given list is empty or not

# method 1
def Enquiry(lst):
	if len(lst) == 0:
		return 0
	else:
		return 1
	
lst = []

if Enquiry(lst):
	print("The list is not empty")
else:
	print("Empty List")



# method 2
l=[]

if len(l)==0:
    print("Empty")
else:
    print('Not Empty')