
for i in range(1, 11, 1):
    for x in range(11, i, -1):
        print(' ', end=' ')
    for y in range(1, i, 1):
        print('*', end=' ')
    for z in range(1, i, 1):
        print('*', end=' ')
    for k in range(11, i, -1):
        print(' ', end=' ')
    print()
    
for i in range(1, 11, 1):
    for m in range(1, i, 1):
        print(' ', end=' ')
    for n in range(11, i, -1):
        print('*', end=' ')
    for o in range(11, i, -1):
        print('*', end=' ')
    for p in range(1, i, 1):
        print(' ', end=' ')
    print()