# Python program to map two list into dictionary

keys=['red','green','blue']
values=['#FF0000','#008000','#0000FF']

color_dict=dict(zip(keys,values))           # we use zip function for this program zip will make key value pairs of different lists

print(color_dict)