amount = int(input("Enter amount to deposit: "))

print("Here is a breakdown of the deposit amount:")
thousand = amount // 1000
amount = amount % 1000
five_hundred = amount // 500
amount = amount % 500
two_hundred = amount // 200
amount = amount % 200
one_hundred = amount // 100
amount = amount % 100
fifthy = amount // 50
amount = amount % 50
twenty = amount // 20
amount = amount % 20
ten = amount // 10
amount = amount % 10
five = amount // 5
amount = amount % 5
one = amount // 1
amount = amount % 1

print("P1,000 -", thousand)
print("P500 -", five_hundred)
print("P200 -", two_hundred)
print("P100 -", one_hundred)
print("P50 -", fifthy)
print("P20 -", twenty)
print("P10 -", ten)
print("P5 -", five)
print("P1 -", one)