
l=[1, 3, 9, "jsca", 5, False, 100, 8, "python", 32, 57, 99, 6, 0, True, 55, "django", 64, 37, "@"]

print(l[:1])
print(l[18:])
print(l[::19])
print(l[1:5:3])
print(l[1:18:20])
print(l[:5:5])
print(l[10::10])
# print(l[4:19:-1])       # minus jump will only work with [::-1] start to end value

print(l[:-16])
print(l[:-1:])
print(l[::-10])
print(l[-17:-10:3])
print(l[-19:-1:8])
print(l[:-4:7])
print(l[:-13:7])
print(l[::-3])