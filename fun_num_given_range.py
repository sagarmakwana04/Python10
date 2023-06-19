# Python function to check whether a number is in a given range


def test_range(n):
    if n in range(1,11):
        print(f'{n} is in a given range')
    else:
        print(f'{n} is a out of range')

test_range(3)
test_range(15)
test_range(0)