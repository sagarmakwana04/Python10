# Program to Return the Length of the Longest Word from the List of Words

def longestlength(a):
    max1=len(a[0])
    temp=a[0]

    for i in a:
        if (len(i)>max1):
            max1=len(i)
            temp=i

    print(f"The word with longest length is '{temp}' and its length is : {max1}")

a=["one","two","third","four"]
longestlength(a)
