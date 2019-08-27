def calc(opr):
    num_1 = input("Enter first number : ")
    num_2 = input("Enter second number : ")
    # if ch == "1":
    #     return num_1 + num_2
    # elif ch == "2":
    #     return num_1 - num_2

    expression = num_1 + opr + num_2
    # print(expression)
    result = eval(expression)
    print(result)

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
    1 : "+",
    2 : "-",
    3 : "/",
    4 : "*"
}

opr = operations.get(ch)
calc(opr)