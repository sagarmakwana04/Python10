# Program to Return the Length of the Longest Word from the List of Words

# Method 1 using for loop
def longestWord(l):
    max1=len(l[0])
    temp=l[0]

    for i in l:
        if len(i)>max1:
            max1=len(i)
            temp=i

    print(f"The word with longest length is '{temp}' and its length is : {max1}")

l=["one","two","three","four"]
longestWord(l)


# Method 2 using max() function
def longestLength(words):
    result=max(words,key=len)
    print(f"The longest word is : {result}, with length of : {len(result)}")

words=["one","two","three","four",'Eighteen']
longestLength(words)

