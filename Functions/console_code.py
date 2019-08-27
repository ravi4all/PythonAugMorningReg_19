Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def sayHello():
	print("Hello User")

	
>>> def sayBye():
	print("Bye User")

	
>>> sayBye
<function sayBye at 0x000001CCD119C1E0>
>>> sayBye()
Bye User
>>> d = {"1":sayHello(),"2":sayBye()}
Hello User
Bye User
>>> d = {"1":sayHello,"2":sayBye}
>>> d
{'1': <function sayHello at 0x000001CCD377B268>, '2': <function sayBye at 0x000001CCD119C1E0>}
>>> d["1"]
<function sayHello at 0x000001CCD377B268>
>>> d["1"]()
Hello User
>>> x = d["1"]
>>> x
<function sayHello at 0x000001CCD377B268>
>>> x()
Hello User
>>> l = [sayBye,sayHello]
>>> l[0]
<function sayBye at 0x000001CCD119C1E0>
>>> l[0]()
Bye User
>>> d
{'1': <function sayHello at 0x000001CCD377B268>, '2': <function sayBye at 0x000001CCD119C1E0>}
>>> d.get['1']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d.get['1']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d.get('1')
<function sayHello at 0x000001CCD377B268>
>>> d.get('1')()
Hello User
>>> "12" + '/' + '14'
'12/14'
>>> eval('12'+'/'+'12')
1.0
>>> '12+3-45/3*34+2/3-45'
'12+3-45/3*34+2/3-45'
>>> 
