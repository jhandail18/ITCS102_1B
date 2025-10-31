name = input("Enter your name: ")
print("++++++++++++++++++++++++")
print("ODD NUMBER SUMMATION, PRESS 0 TO STOP")
print("++++++++++++++++++++++++")

sum = 0
odd = ""
while True:
    number = eval(input("Enter any number: "))
    
    if number == 0:
        print("STOP!!")
        break
    
    elif number % 2 == 1:
        print("ODD NUMBER DETECTED, CONTINUE.. ")
        sum += number
        odd += str(number) + " "
        continue
    
    elif number % 2 == 0:
        print("EVER NUMBER DETECTED, CONTINUE..")
        continue
    
    else:
        print("Invalid Input")
        
print(f"Hello {name}, the sum of all ODD numbers is {sum}")
print(f"ODD numbers detected included the ff {odd}")