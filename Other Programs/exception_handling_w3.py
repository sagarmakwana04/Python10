try:
    print("Hello")
except :
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    print("the try except is finished")


# x=-1
# if x<0:
#     raise Exception("Sorry, no number below zero")


x="hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")
    