# Python program to combine values in python list of dictionaries.

from collections import Counter

# Exa - 1
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

dct=Counter(d1) + Counter(d2)
print(dct)



# Exa - 2
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()

for d in item_list:
    result[d['item']] += d['amount']
print(result)