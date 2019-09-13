Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y):
	return x + y

>>> add(4,5)
9
>>> x = 2
>>> y = 3
>>> add(x,y)
5
>>> def sub(x,y):
	return x - y

>>> def calc():
	x1 = 12
	y1 = 21
	print(add(x1,y1))
	print(sub(x1,y1))

	
>>> calc()
33
-9
>>> x1 - y1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    x1 - y1
NameError: name 'x1' is not defined
>>> x
2
>>> y
3
>>> def counter(x):
	print("Started...")
	return x+1

>>> count(4)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    count(4)
NameError: name 'count' is not defined
>>> counter(4)
Started...
5
>>> def counter(x):
	print("Started...")
	while x < 10:
		x = x + 1
		return x

	
>>> counter(0)
Started...
1
>>> counter(0)
Started...
1
>>> def counter(x):
	print("Started...")
	while x < 10:
		x = x + 1
		yield x

		
>>> counter(0)
<generator object counter at 0x000001EABC137840>
>>> list(counter(0))
Started...
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for n in list(counter(0)):
	print(n)

	
Started...
1
2
3
4
5
6
7
8
9
10
>>> counter(0)
<generator object counter at 0x000001EABC137840>
>>> val = counter(0)
>>> val
<generator object counter at 0x000001EABC16A750>
>>> next(val)
Started...
1
>>> next(val)
2
>>> next(val)
3
>>> next(val)
4
>>> next(val)
5
>>> next(val)
6
>>> next(val)
7
>>> 7
7
>>> next(val)
8
>>> next(val)
9
>>> next(val)
10
>>> next(val)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    next(val)
StopIteration
>>> def counter(x):
	print("Started...")
	while x < 10:
		x = x + 1
		return x

	
>>> val = counter(0)
Started...
>>> val
1
>>> next(val)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    next(val)
TypeError: 'int' object is not an iterator
>>> def counter(x):
	print("Started...")
	while x < 10:
		yield x
		x = x + 1

		
>>> val = counter(0)
>>> next(val)
Started...
0
>>> next(val)
1
>>> next(val)
2
>>> next(val)
3
>>> next(val)
4
>>> next(val)
5
>>> next(val)
6
>>> next(val)
7
>>> next(val)
8
>>> next(val)
9
>>> next(val)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    next(val)
StopIteration
>>> x = [i**2 for i in range(1,10)]
>>> x
[1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x = (i**2 for i in range(1,10))
>>> x
<generator object <genexpr> at 0x000001EABC16A840>
>>> import sys
>>> x1 = [i**2 for i in range(1,10)]
>>> sys.getsizeof(x1)
192
>>> x2 = (i**2 for i in range(1,10))
>>> sys.getsizeof(x2)
120
>>> x1 = [i**2 for i in range(1,10000)]
>>> sys.getsizeof(x2)
120
>>> sys.getsizeof(x1)
87624
>>> x2 = (i**2 for i in range(1,10000))
>>> sys.getsizeof(x2)
120
>>> import cProfile
>>> cProfile.run(x1)
         2 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    cProfile.run(x1)
  File "C:\Python37\lib\cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "C:\Python37\lib\profile.py", line 53, in run
    prof.run(statement)
  File "C:\Python37\lib\cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "C:\Python37\lib\cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
TypeError: exec() arg 1 must be a string, bytes or code object
>>> exec()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    exec()
TypeError: exec expected at least 1 arguments, got 0
>>> exec('[i**2 for i in range(1,10000)]')
>>> exec([i**2 for i in range(1,10)])
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    exec([i**2 for i in range(1,10)])
TypeError: exec() arg 1 must be a string, bytes or code object
>>> exec('[i**2 for i in range(1,10)]')
>>> cProfile.run('[i**2 for i in range(1,10000)]')
         4 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.005    0.005 <string>:1(<listcomp>)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('(i**2 for i in range(1,10000))')
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('(i**2 for i in range(1,1000000))')
         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<genexpr>)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> cProfile.run('[i**2 for i in range(1,1000000)]')
         4 function calls in 0.518 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.504    0.504    0.504    0.504 <string>:1(<listcomp>)
        1    0.014    0.014    0.517    0.517 <string>:1(<module>)
        1    0.000    0.000    0.518    0.518 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


>>> 
