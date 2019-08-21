# 1
# 2 3
# 4 5 6
# 7 8 9 10
k = 0
for i in range(1,5):
    for j in range(i):
        k += 1
        print(k,end='')
    print()