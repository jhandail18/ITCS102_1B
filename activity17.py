# nested for loop

# for i in range(1,11,1):
#     print(i)

for i in range(1,11,1):
    # print(i,end="-")
    for x in range(1,11,1):
        print(x, end=" ")
    print()
        
        
# 2
for i in range(1,11,1):
    for x in range(1, i ,1):
        print(x, end=" ")
    print(i)
    
