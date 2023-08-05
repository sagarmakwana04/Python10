# Python program to find longest word in file
# 1.open file, 2.words split(), 3.find max_len word, 4.return if word==max len


def longest_word(fname):
    with open(fname)as f:
        words=f.read().split()
    max_len=len(max(words,key=len))
    return [word for word in words if len(word)==max_len]

print(longest_word('test.txt'))
print(longest_word('test2.txt'))
print(longest_word('test3.txt'))