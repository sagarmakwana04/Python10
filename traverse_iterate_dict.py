# Python program to traverse/iterate in dictionary

# using .keys() function
statesAndCapitals={'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur','Bihar':'Patna'}
keys=statesAndCapitals.keys()
print(keys)


# using for loop, without .keys() function
for states in statesAndCapitals:
    print(states)