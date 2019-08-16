Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> msg = "hi"
>>> data = ["hello","hi","hey","hi there","hello there"]
>>> data[0]
'hello'
>>> data[1]
'hi'
>>> data[2]
'hey'
>>> data[1] == msg
True
>>> data[2] == msg
False
>>> for i in range(len(data)):
	if data[i] ==  msg:
		print("Found")
		break

	
Found
>>> msg in data
True
>>> import datetime
>>> import time
>>> time.ctime()
'Fri Aug 16 11:09:07 2019'
>>> datetime.datetime.now()
datetime.datetime(2019, 8, 16, 11, 9, 29, 421254)
>>> datetime.datetime.now().date()
datetime.date(2019, 8, 16)
>>> datetime.datetime.now().time()
datetime.time(11, 9, 54, 718356)
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 8, 16, 11, 10, 16, 374414)
>>> date = datetime.now().date()
>>> date
datetime.date(2019, 8, 16)
>>> print(date)
2019-08-16
>>> date.strftime("%d/%m/%y,%p")
'16/08/19,AM'
>>> date.strftime("%d/%m/%y,%a")
'16/08/19,Fri'
>>> t = datetime.now().time()
>>> t
datetime.time(11, 12, 29, 954967)
>>> print(t)
11:12:29.954967
>>> t.strftime("%H:%M:%S,%P")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    t.strftime("%H:%M:%S,%P")
ValueError: Invalid format string
>>> t.strftime("%H:%M:%S,%p")
'11:12:29,AM'
>>> for i in range(10):
	t = datetime.now().time()
	print(t.strftime("%H:%M:%S,%p"))
	time.sleep(1)

	
11:13:53,AM
11:13:54,AM
11:13:55,AM
11:13:56,AM
11:13:57,AM
11:13:58,AM
11:13:59,AM
11:14:00,AM
11:14:01,AM
11:14:02,AM
>>> for i in range(10):
	t = datetime.now().time()
	print(t.strftime("%H:%M:%S,%p"))

	
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
11:14:08,AM
>>> import os
>>> os.system('calc')
0
>>> os.system('notepad')
0
>>> os.startfile('C:\Users\asus\Music\Billian-Billian-Guri.mp3')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.startfile(r'C:\Users\asus\Music\Billian-Billian-Guri.mp3')
>>> os.chdir(r'C:\Users\asus\Music)
	 
SyntaxError: EOL while scanning string literal
>>> os.chdir(r'C:\Users\asus\Music')
>>> os.getcwd()
'C:\\Users\\asus\\Music'
>>> songs = os.listdir()
>>> songs
['5-Varlaam Varlaam Vaa-SenSongsMp3.Co.mp3', 'BIGGEST BASS DROP EVER! (EXTREME BASS TEST!!!).mp3', 'Billian-Billian-Guri.mp3', 'Cristiano Ronaldo - Faded Best Moments 2017 • 100.000 Subscribers.mp3', 'desktop.ini', 'Dub Theri Step with Lyrics   Theri   Vijay, Samantha, Amy Jackson   Atlee   G.V.Prakash Kumar.ogg', 'Ek Pal Ka Jeena-(Mr-Jatt.com).mp3', 'Kaththi Theme…The Sword of Destiny - Full Audio.ogg', 'music_1.ogg', 'Na Ja.mp3', 'Shape of You.mp3', 'Street Fighter V Soundtrack - Main Menu.ogg', "Street Fighter V Soundtrack - Ryu's Theme.ogg", 'StreetFighter.mp3', 'Vedalam - The Theri Theme Lyric   Ajith Kumar, Shruti Haasan   Anirudh.ogg']
>>> import random
>>> song = random.choice(songs)
>>> song
'Shape of You.mp3'
>>> os.startfile(song)
>>> 
