import random
def temp_conv(cel):
    return 9/5 * cel + 32

temp = []
for i in range(10):
    t = round(random.uniform(30,40),2)
    temp.append(t)

# f = list(map(temp_conv, temp))
# print(f)

def myMap(func,iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = myMap(temp_conv, temp)
print(f)