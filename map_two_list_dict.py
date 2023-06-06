# Python program to map two list into dictionary

# we use zip function for this program 

keys=['red','green','blue']
values=['#FF0000','#008000','#0000FF']
color_dictionary=dict(zip(keys,values))
print(color_dictionary)