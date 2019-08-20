Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello this is Python Programming"
>>> text[0]
'H'
>>> text[12]
's'
>>> text[0:4]
'Hell'
>>> text[4:10]
'o this'
>>> text[0:20:2]
'Hloti sPto'
>>> text[-1]
'g'
>>> text[10:2]
''
>>> text[10:2:-1]
' siht ol'
>>> text[10:1:-1]
' siht oll'
>>> text[10:0:-1]
' siht olle'
>>> text[10::-1]
' siht olleH'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text
'Hello this is Python Programming'
>>> text.lower()
'hello this is python programming'
>>> text.upper()
'HELLO THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello this is python programming'
>>> text.title()
'Hello This Is Python Programming'
>>> text.count(o)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    text.count(o)
NameError: name 'o' is not defined
>>> text.count('o')
3
>>> text.find('o')
4
>>> text.find('o',5)
18
>>> text.find('o',19)
23
>>> text.rfind('o')
23
>>> text.center(50)
'         Hello this is Python Programming         '
>>> len(text)
32
>>> text.center(32)
'Hello this is Python Programming'
>>> text.center(33)
' Hello this is Python Programming'
>>> text.center(34)
' Hello this is Python Programming '
>>> text.center(50)
'         Hello this is Python Programming         '
>>> text = text.center(50)
>>> text
'         Hello this is Python Programming         '
>>> text.strip()
'Hello this is Python Programming'
>>> text = text.center(50,'*')
>>> text
'         Hello this is Python Programming         '
>>> text = text.zfill(50,'*')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    text = text.zfill(50,'*')
TypeError: zfill() takes exactly one argument (2 given)
>>> text
'         Hello this is Python Programming         '
>>> text = text.strip()
>>> text = text.center(50,'*')
>>> text
'*********Hello this is Python Programming*********'
>>> text = text.strip()
>>> text
'*********Hello this is Python Programming*********'
>>> text = text.strip('*')
>>> text
'Hello this is Python Programming'
>>> text.split()
['Hello', 'this', 'is', 'Python', 'Programming']
>>> text = text.split()
>>> text
['Hello', 'this', 'is', 'Python', 'Programming']
>>> '-'.join(text)
'Hello-this-is-Python-Programming'
>>> '->'.join(text)
'Hello->this->is->Python->Programming'
>>> text= ' '.join(text)
>>> text
'Hello this is Python Programming'
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.startswith('x')
False
>>> text.startswith('H')
True
>>> text.startswith('h')
False
>>> text
'Hello this is Python Programming'
>>> text += "Ok"
>>> text
'Hello this is Python ProgrammingOk'
>>> del text[0]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    del text[0]
TypeError: 'str' object doesn't support item deletion
>>> text[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    text[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
