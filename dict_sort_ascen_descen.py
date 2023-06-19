# Python script to sort ascending and descending a dinctionary by value

import operator

dct={1:'A',2:'B',3:'C'}

sort_dct=sorted(dct.items(), key=operator.itemgetter(1))
print(sort_dct)

sort_dct=sorted(dct.items(), key=operator.itemgetter(1), reverse=True)
print(sort_dct)