Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> emp = ['Ram',45000,'IT']
>>> emp
['Ram', 45000, 'IT']
>>> even = []
>>> even.append(2)
>>> even.append(4)
>>> even = []
>>> for i in range(51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> even.pop()
50
>>> even.pop(6)
12
>>> even.insert(4,15)
>>> even
[0, 2, 4, 6, 15, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> list_1 = [5,9,12,31,5,43,67,3,6,87,54,]
>>> even.append(list_1)
>>> even
[0, 2, 4, 6, 15, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, [5, 9, 12, 31, 5, 43, 67, 3, 6, 87, 54]]
>>> even.pop()
[5, 9, 12, 31, 5, 43, 67, 3, 6, 87, 54]
>>> even.extend(list_1)
>>> even
[0, 2, 4, 6, 15, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 5, 9, 12, 31, 5, 43, 67, 3, 6, 87, 54]
>>> even.remove(6)
>>> even
[0, 2, 4, 15, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 5, 9, 12, 31, 5, 43, 67, 3, 6, 87, 54]
>>> even.remove(9)
>>> even
[0, 2, 4, 15, 8, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 5, 12, 31, 5, 43, 67, 3, 6, 87, 54]
>>> even.remove(99)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    even.remove(99)
ValueError: list.remove(x): x not in list
>>> even.sort()
>>> even
[0, 2, 3, 4, 5, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 26, 28, 30, 31, 32, 34, 36, 38, 40, 42, 43, 44, 46, 48, 54, 67, 87]
>>> even.sort(reverse=True)
>>> even
[87, 67, 54, 48, 46, 44, 43, 42, 40, 38, 36, 34, 32, 31, 30, 28, 26, 24, 22, 20, 18, 16, 15, 14, 12, 10, 8, 6, 5, 5, 4, 3, 2, 0]
>>> 4 in even
True
>>> even.index(4)
30
>>> data = ['Ram',20000,'IT','TCS','Delhi']
>>> data_copy = data
>>> a = 12
>>> b = a
>>> c = b
>>> data
['Ram', 20000, 'IT', 'TCS', 'Delhi']
>>> data_copy
['Ram', 20000, 'IT', 'TCS', 'Delhi']
>>> data[1] = 25000
>>> data
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data_copy
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data[:]
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data[0:]
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data[:3]
['Ram', 25000, 'IT']
>>> data[:]
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data_2 = data[:]
>>> data_copy == data
True
>>> data_copy == data_2
True
>>> data_copy is data
True
>>> data is data_2
False
>>> data_2[1] = 30000
>>> data_2
['Ram', 30000, 'IT', 'TCS', 'Delhi']
>>> data
['Ram', 25000, 'IT', 'TCS', 'Delhi']
>>> data = ['Ram', 25000, 'IT', 'TCS', ['Delhi','Pune','Chennai']]
>>> data_2 = data[:]
>>> data_2
['Ram', 25000, 'IT', 'TCS', ['Delhi', 'Pune', 'Chennai']]
>>> data_2[1] = 20000
>>> data_2
['Ram', 20000, 'IT', 'TCS', ['Delhi', 'Pune', 'Chennai']]
>>> data
['Ram', 25000, 'IT', 'TCS', ['Delhi', 'Pune', 'Chennai']]
>>> data_2[-1][0] = 'Noida'
>>> data_2
['Ram', 20000, 'IT', 'TCS', ['Noida', 'Pune', 'Chennai']]
>>> data
['Ram', 25000, 'IT', 'TCS', ['Noida', 'Pune', 'Chennai']]
>>> import copy
>>> data_3 = copy.deepcopy(data)
>>> data_3
['Ram', 25000, 'IT', 'TCS', ['Noida', 'Pune', 'Chennai']]
>>> data_3[-1][0] = 'Delhi'
>>> data_3
['Ram', 25000, 'IT', 'TCS', ['Delhi', 'Pune', 'Chennai']]
>>> data
['Ram', 25000, 'IT', 'TCS', ['Noida', 'Pune', 'Chennai']]
>>> 
