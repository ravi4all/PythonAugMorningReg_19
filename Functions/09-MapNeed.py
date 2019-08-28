import random
def temp_conv(cel):
    return 9/5 * cel + 32

# f = temp_conv(34.4)
# print(f)

temp = []
for i in range(10):
    t = round(random.uniform(30,40),2)
    temp.append(t)

f = []
for t in temp:
    converted = temp_conv(t)
    f.append(converted)

print(f)