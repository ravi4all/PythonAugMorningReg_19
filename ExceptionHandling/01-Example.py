try:
    f_num = int(input("Enter first number : "))
    s_num = int(input("Enter second number : "))

    a = f_num + s_num
    print("Sum is",a)

    b = f_num - s_num
    print("Diff is",a)

    c = f_num / s_num
    print("Div is",a)

    d = f_num * s_num
    print("Mul is",a)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input, Please enter a digit (0-9)")
except BaseException as ex:
    print(ex)