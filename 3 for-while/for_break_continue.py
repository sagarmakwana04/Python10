# break etle loop ne chhodine nikdi jaav
print("Skip the loop")
for i in range(1, 11):
    print("5 x ", i, "=", 5*i)    

    if(i==5):
       
        break
    
print()
# continue etle iteration ne chhodine nikdi jaav
for i in range(1, 11):
    if(i==5):
        print("skip this particular iteration")
        continue
    print("5 x ", i, "=", 5*i)
