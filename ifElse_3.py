name = input("Enter your name : ")
print("Welcome",name)

# Logical Operator - and, or, not
# Comparison Operator - ==, >, <, >=, <=, !=
# Identity Operator - is, not is
# Membership Operator - in, not in

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print("Hi There...")
    elif msg == "bye":
        print("Bye",name,"Have a nice day...")
        chat = False
    else:
        print("I don't understand")
