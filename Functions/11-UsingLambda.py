import random

temp = []
for i in range(10):
    t = round(random.uniform(30,40),2)
    temp.append(t)

f = list(map(lambda t : 9/5 * t + 32, temp))
print(f)