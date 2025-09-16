sum = 0

for i in range(7):
    number = eval(input("Enter any number: "))
    if number % 2 != 0:
        sum += number
        
print("The total of odd number is:",sum)