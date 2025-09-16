sum = 1
number = eval(input("Enter any number: "))

for i in range(number, 0, -1):
    sum *= i
print("The factorial of", number, "is", sum)