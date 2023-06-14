


def first_last_two(s):
    length=len(s)
    if length>2:
        return s[:2] + s[-2:]
    else:
        return s
    
print(first_last_two('python program'))