print("Break will leave the loop")
for i in range(1, 11):
    print(i)    
    if(i==5):
        break
    

print()
for i in range(1, 11):
    if(i==5):
        print("Continue will skip the particular iteration")
        continue
    print(i)
