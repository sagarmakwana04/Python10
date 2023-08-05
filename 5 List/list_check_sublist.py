# Python program to check whether a list contains a sub list 

# l=[1,2,3,4,5,[6,7,8,9,0]]

def isSublist(l,s):
    sub_set=False
    if s==[]:
        sub_set=True
    elif s==l:
        sub_set=True
    elif len(s)>len(l):
        sub_set=False
    
    else:
        for i in range(len(l)):
            if l[i]==s[0]:
                n=1
                while (n<len(s)) and (l[i+n]==s[n]):
                    n+=1
                
                if n==len(s):
                    sub_set=True
    return sub_set

a=[2,4,3,5,7]
b=[4,3]
c=[3,7]
print(isSublist(a,b))
print(isSublist(a,c))