Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 21
>>> b = 44
>>> c = a + b
>>> print(c)
65
>>> print c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(c)?
>>> 12 / 7
1.7142857142857142
>>> True = False
SyntaxError: can't assign to keyword
>>> input("Enter your name : ")
Enter your name : Ravi
'Ravi'
>>> 2 ** 7
128
>>> 2 ** 15
32768
>>> a = 12
>>> name = "Ravi"
>>> id(name)
2895014556256
>>> id("Ravi")
2895014556256
>>> id(12)
140720145720304
>>> id(4)
140720145720048
>>> a = 12
>>> id(a)
140720145720304
>>> a = "hello ram how are you ?"
>>> a.encode()
b'hello ram how are you ?'
>>> a = "हैलो राम आप कैसे हैं?"
>>> a.encode()
b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82?'
>>> x = b'\xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\xb2\xe0\xa5\x8b \xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xae'
>>> x.decode()
'हैलो राम'
>>> 
