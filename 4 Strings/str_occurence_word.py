# To Count occurence of each word in a given string

s='jsca hello jay hello jsca jay happy jsca'

def count_word(str):                
    count=dict()                    # store words into dict to get its key and value pair
    words=str.split()               # to stplit all words of given string other wise loop will consider it as letters instead of words
    for word in words:              # to get word from all words
        if word in count:           # if word is already exist in dict named count then add 1 to its value
            count[word]+=1          
        else:
            count[word]=1           # else take its value as 1 if that word comes once only
    return count                    # return count

print(count_word(s))