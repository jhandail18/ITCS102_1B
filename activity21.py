isClean = True

while isClean == True:
    qst = input("Are the Clothes Clean? (y/n): ")
    
    if qst.lower() == 'y':
        print("Loop Continue..")
        continue
    
    else:
        print("Loop Stop.")
        break