# Scope of variables - local and global
x = 10
y = 6
def add():
    global x
    x = 12
    # y = 33
    z = x + y
    print(z)

add()
print(x - y)