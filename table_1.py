num = int(input("Enter the number : "))

'''
for i in range(num,num*10 + 1,num):
    print(i)
'''

for i in range(1,11):
    print("{} x {} = {}".format(num,i,num * i))
