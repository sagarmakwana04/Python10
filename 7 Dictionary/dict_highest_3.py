# Python program to find the highest 3 values in a dictionary

from collections import Counter

my_dict={'A':67,'B':23,'C':57,'D': 56, 'E': 12, 'F': 69}

k=Counter(my_dict)

print(k.most_common(3))
