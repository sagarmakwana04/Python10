# to check time taken in list comprehension

import time

def list_comprehension(num):
    [i+10 for i in range(num)]

start=time.time()
list_comprehension(10000000)
end=time.time()

print("Time taken by list comprehension:",(end-start))