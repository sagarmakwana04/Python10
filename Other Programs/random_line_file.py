# Python program to read a random line from a file

import random

lines=open('copy.txt').read().splitlines()
print(random.choice(lines))


# def random_line(fname):
#     lines = open(fname).read().splitlines()
#     return random.choice(lines)
# print(random_line('test.txt'))