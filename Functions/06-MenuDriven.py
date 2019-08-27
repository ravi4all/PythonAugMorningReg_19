def takeInput():
    num_1 = int(input("Enter first number : "))
    num_2 = int(input("Enter second number : "))
    return num_1,num_2

def add():
    x, y = takeInput()
    z = x + y
    print(z)

def sub():
    x,y = takeInput()
    z = x - y if x > y else y - x
    print(z)

def div():
    x,y = takeInput()
    z = x / y
    print(z)

def mul():
    x,y = takeInput()
    z = x * y
    print(z)

def err(*args,**kwargs):
    print("Invalid Choice")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = int(input("Enter your choice : "))

operations = {
    1 : add,
    2 : sub,
    3 : div,
    4 : mul
}

# operations[ch](num_1,num_2)
operations.get(ch,err)()