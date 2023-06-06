# Python script to sort ascending and descending a dinctionary by value

import operator

d={20:'b',30:'c',10:'a'}
print('Original Dinctionary : ',d)

sorted_d=sorted(d.items(), key=operator.itemgetter(1))
print(f"Ascending order by value : {sorted_d}")
sorted_d=sorted(d.items(), key=operator.itemgetter(1),reverse=True)
print(f"Descending order by value : {sorted_d}")