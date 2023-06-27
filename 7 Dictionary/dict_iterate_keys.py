# Python program to traverse/iterate in dictionary

# using .keys() function
statesAndCapitals={'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur','Bihar':'Patna'}
print(statesAndCapitals.keys())         # gives keys in list form


# using for loop, without .keys() function
for states in statesAndCapitals:            # for loop can only gives keys
    print(states, end=' ')                           # statesAndCapitals[states] - will print only values