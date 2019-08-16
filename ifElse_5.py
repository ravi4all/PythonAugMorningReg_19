from datetime import datetime
import os, random

name = input("Enter your name : ")
print("Welcome",name)

helloIntent = ["hi","hello","hey","hi jarvis","hey jarvis","hello jarvis"]
dateIntent = ["tell me date","date please","what's the date","today's date","date"]
timeIntent = ["tell me time","time please","what's the time","current time","time"]
musicIntent = ["play music","play song","start music","please play a song"]


chat = True
while chat:
    msg = input("Enter your message : ")
    msg = msg.lower()
    if msg in helloIntent:
        print("Hi There...")
    elif msg in dateIntent:
        cur_date = datetime.now().date()
        print(cur_date.strftime("%d/%m/%y,%a"))
    elif msg in timeIntent:
        cur_time = datetime.now().time()
        print(cur_time.strftime("%H/%M/%S,%p"))
    elif msg in musicIntent:
        path = r"C:\Users\asus\Music"
        os.chdir(path)
        songs = os.listdir()
        song = random.choice(songs)
        print("Playing =>",song)
        os.startfile(song)
    elif msg == "bye":
        print("Bye",name,"Have a nice day...")
        chat = False
    else:
        print("I don't understand")
