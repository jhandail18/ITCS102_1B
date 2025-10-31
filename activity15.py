#STRING CONCATENATION

fname = 'jhandail'
mname = 'perdigones'
lname = 'furuc'

print("My full name is", fname, mname, lname)


# f string
fname = 'jhandail'
mname = 'perdigones'
lname = 'furuc'

print(f"My full name is {fname.upper()} {mname} {lname}")

# 2
fname = 'jhandail'
mname = 'perdigones'
lname = 'furuc'


# 3
sum = 0 
for i in range(1, 6):
    x  = eval(input(f"{i} - Input a number --> "))
    sum += x 
print(f"The total sum is {sum}")