name = input("Enter your name : ")
print("Welcome",name)

helloIntent = ["hi","hello","hey","hi jarvis","hey jarvis","hello jarvis"]

chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hi There...")
    elif msg == "bye":
        print("Bye",name,"Have a nice day...")
        chat = False
    else:
        print("I don't understand")
