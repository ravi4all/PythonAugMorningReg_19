# def calc(x,y):
#     z = x + y
#     print(z)
#     return z

def calc(x,y):
    return x + y, x * y, x - y, x / y

# s = calc(4,5)
# print(s)

# a,b,c,d = calc(4,5)
# print(a,b,c,d)

a,b,*c = calc(4,5)
print(a,b,c)