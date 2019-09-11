def atm(total):
    pin = input("Enter your pin : ")
    if pin == "1234":
        print("Login Success")
    else:
        raise ValueError("Login Failed, Invalid Pin")

    amt = int(input("Enter the amount you want to withdraw : "))
    if amt < total:
        total -= amt
        print("Transaction Successful")
        print("Remaining balance is",total)
    else:
        raise ValueError("Insufficient Balance")

try:
    atm(5000)
except ValueError as err:
    print(err)
    atm(5000)