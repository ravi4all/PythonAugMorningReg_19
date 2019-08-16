Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 12
>>> b = 21
>>> c = a + b
>>> print(c)
33
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
>>> a
12
>>> b
33
>>> a - b
-21
>>> a / b
0.36363636363636365
>>> a * b
396
>>> 12 / 5
2.4
>>> 12 // 5
2
>>> 45 / 8
5.625
>>> 45 // 8
5
>>> 45 ** 4
4100625
>>> 45 ** 2
2025
>>> 
>>> 45 ** 20
1159445329576199417209625244140625
>>> a,b = 11,44
>>> a,b = b,a
>>> a
44
>>> b
11
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
>>> name = "Ravi"
>>> msg = "Hello " + name
>>> msg
'Hello Ravi'
>>> name = "Ram"
>>> sal = 10000
>>> msg = "Name is "+ name + "and" + "salary is" + sal
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    msg = "Name is "+ name + "and" + "salary is" + sal
TypeError: can only concatenate str (not "int") to str
>>> msg = "Name is {} and salary is {}".format(name,sal)
>>> msg
'Name is Ram and salary is 10000'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45

1. Add
2. Sub
3. Div
4. Mul

>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/01-code.py 
Sum is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45
Sum of 12 and 33 is 45

1. Add is 45
2. Sub is -21
3. Div is 0.36363636363636365
4. Mul is 396

>>> a = "hello world"
>>> print(a)
hello world
>>> a = "hello "world""
SyntaxError: invalid syntax
>>> a = 'hello "world"'
>>> print(a)
hello "world"
>>> a = "hello \"world\""
>>> print(a)
hello "world"
>>> a = "hello \n world"
>>> print(a)
hello 
 world
>>> a = "hello \\n world"
>>> print(a)
hello \n world
>>> a = """'hello "world"'"""
>>> print(a)
'hello "world"'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/02-code.py 
Enter your name : Ram
Hello Ram
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/02-code.py 
Enter your name : Ram
Hello Ram
Enter your sal : 12000
Traceback (most recent call last):
  File "C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/02-code.py", line 6, in <module>
    total_sal = sal + incentive
TypeError: can only concatenate str (not "int") to str
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/02-code.py 
Enter your name : Ram
Hello Ram
Enter first number : 12
Enter second number : 67
Sum is 1267
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Aug/PythonMorningReg/02-code.py 
Enter your name : Ram
Hello Ram
Enter your sal : 34000
Your total salary is 39000
>>> 
