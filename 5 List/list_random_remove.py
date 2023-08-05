
# import random

# # To generate random number from (1,100)
# print(random.randint(1, 50))


# # To generate random from given list
# print(random.choice([1, 29, 56, 38, True, False, "python", "jsca", 0, 4, 9]))


# # Generate 100 number in a list, then generate 10 random number from that list and remove those random number from 100 num list
# l=[]                           
# lucky=[]                        

# for i in range(1,101):           # 1. create list of 100 num
#     l.append(i)

# for i in range(10):              # 2. create list of 10 num
#     num=random.choice(l)         # 3. store those 10 num into random.choice(l)
#     lucky.append(num)            # 4. lucky.append(num)  append those 10 random word into lucky named list
#     l.remove(num)                # 5. remove those from main list named l 

# print(l)
# print(lucky)