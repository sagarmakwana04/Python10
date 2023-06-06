# Python function to check whether a number is in a given range

def test_range(n):
    if n in range(2,9):
        print("%s is in the range"%str(n))
    else:
        print("The number is outof given range.")
test_range(7)
test_range(4)
test_range(91)