# Python program to pick random item from range

import random

x=random.randrange(1,51)
print(f'Random : {x}')


# to generate odd number randomly from range
y=random.randrange(1,50,2)
print(f"Odd Random : {y}")


# to generate even number randomly from range
z=random.randrange(0,50,2)
print(f"Even Random : {z}")