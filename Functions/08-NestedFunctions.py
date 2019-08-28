def calc():
    x = 12
    y = 34

    def add():
        return x  + y

    def sub():
        return x - y

    return add,sub

a,b = calc()
print("Addition is",a())
print("Subtraction is",b())