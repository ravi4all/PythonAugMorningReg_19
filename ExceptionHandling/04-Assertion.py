def atm(total):
    pin = input("Enter your pin : ")
    assert (pin == "1234"),"Login Failed, Invalid Pin"
    print("Login Success")

    amt = int(input("Enter the amount you want to withdraw : "))
    assert (amt < total),"Insufficient Balance"
    total -= amt
    print("Transaction Successful")
    print("Remaining balance is",total)

try:
    atm(5000)
except AssertionError as err:
    print(err)
    atm(5000)