Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Repeat():
	def __init__(self,value):
		self.value = value
	def __iter__(self):
		return self
	def __next__(self):
		return self.value

	
>>> rep = Repeat("Hello")
>>> rep
<__main__.Repeat object at 0x0000028751427978>
>>> for item in rep:
	print(item)

	
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Traceback (most recent call last):
  File "<pyshell#12>", line 2, in <module>
    print(item)
KeyboardInterrupt
>>> class Repeat():
	def __init__(self,value,maxCount):
		self.value = value
		self.count = 0
		self.maxCount = maxCount
	def __iter__(self):
		return self
	def __next__(self):
		if self.count >= self.maxCount:
			raise StopIteration
		self.count += 1
		return self.value

	
>>> rep = Repeat("Hello")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    rep = Repeat("Hello")
TypeError: __init__() missing 1 required positional argument: 'maxCount'
>>> rep = Repeat("Hello",5)
>>> for item in rep:
	print(item)

	
Hello
Hello
Hello
Hello
Hello
>>> import itertools
>>> x = [1,2,3,4,5,6]
>>> y = ['a','b','c','d','e','f']
>>> zip(x,y)
<zip object at 0x000002875148E548>
>>> list(zip(x,y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
>>> for i,j in zip(x,y):
	print(i,j)

	
1 a
2 b
3 c
4 d
5 e
6 f
>>> x = [1,2,3,4,5,6,7,8]
>>> y = ['a','b','c','d','e','f']
>>> list(zip(x,y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f')]
>>> itertools.zip_longest(x,y)
<itertools.zip_longest object at 0x00000287514E9A48>
>>> list(itertools.zip_longest(x,y))
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, None), (8, None)]
>>> x = [1,2,3,4]
>>> itertools.combinations(x,3)
<itertools.combinations object at 0x00000287514E9A48>
>>> list(itertools.combinations(x,3))
[(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
>>> list(itertools.combinations(x,4))
[(1, 2, 3, 4)]
>>> list(itertools.combinations(x,2))
[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
>>> list(itertools.permutations(x,4))
[(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 3, 4, 2), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (2, 3, 1, 4), (2, 3, 4, 1), (2, 4, 1, 3), (2, 4, 3, 1), (3, 1, 2, 4), (3, 1, 4, 2), (3, 2, 1, 4), (3, 2, 4, 1), (3, 4, 1, 2), (3, 4, 2, 1), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 2, 3, 1), (4, 3, 1, 2), (4, 3, 2, 1)]
>>> list(itertools.permutations(x,3))
[(1, 2, 3), (1, 2, 4), (1, 3, 2), (1, 3, 4), (1, 4, 2), (1, 4, 3), (2, 1, 3), (2, 1, 4), (2, 3, 1), (2, 3, 4), (2, 4, 1), (2, 4, 3), (3, 1, 2), (3, 1, 4), (3, 2, 1), (3, 2, 4), (3, 4, 1), (3, 4, 2), (4, 1, 2), (4, 1, 3), (4, 2, 1), (4, 2, 3), (4, 3, 1), (4, 3, 2)]
>>> list(itertools.permutations(x,2))
[(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
>>> import functools
>>> def multiplier(x,y):
	return x * y

>>> multiplier(2,3)
6
>>> def doubleIt(x,y=2):
	return multiplier(x,y)

>>> def tripleIt(x,y=3):
	return multiplier(x,y)

>>> doubleIt(2)
4
>>> tripleIt(5)
15
>>> functools.partial(multiplier,2,3)
functools.partial(<function multiplier at 0x00000287514BFC80>, 2, 3)
>>> functools.partial(multiplier,2,3)()
6
>>> functools.partial(multiplier,2,5)()
10
>>> functools.partial(multiplier,2,10)()
20
>>> d = functools.partial(multiplier,2,10)
>>> d
functools.partial(<function multiplier at 0x00000287514BFC80>, 2, 10)
>>> d.keywords
{}
>>> d = functools.partial(multiplier,2,y=10)
>>> d
functools.partial(<function multiplier at 0x00000287514BFC80>, 2, y=10)
>>> d()
20
>>> d.keywords
{'y': 10}
>>> d.
SyntaxError: invalid syntax
>>> d.args
(2,)
>>> multiplier(2,10)
20
>>> import collections
>>> collections.Counter
<class 'collections.Counter'>
>>> collections.Counter()
Counter()
>>> x = collections.Counter([3,6,7,3,6])
>>> x
Counter({3: 2, 6: 2, 7: 1})
>>> 
