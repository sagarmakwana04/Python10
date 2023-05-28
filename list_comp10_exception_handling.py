l1=[3,5,6,22,3,5,88,-3,20]
l2=[1,4,6,3,29,0,37]

def until_func(a,b):
    try:
        return round(a/b,3)
    except ZeroDivisionError as e:
        print("Division by zero not allowed")

l3=[until_func(x,y) for x,y in zip(l1,l2)]
print(l3)
