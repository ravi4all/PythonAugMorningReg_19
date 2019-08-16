for i in range(1,7):
    for j in range(i):
        print('*',end='')
    print()

for i in range(10):
    for j in range(10 - i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()
