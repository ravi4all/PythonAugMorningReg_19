Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 12,45,67,3,5,7,32
>>> x = 12
>>> x = 12,
>>> x = (12,45,67,3,5,7,32)
>>> x[0]
12
>>> x[0:3]
(12, 45, 67)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> emp = name,sal,dept = 'Ram',24000,'IT'
>>> name
'Ram'
>>> sal
24000
>>> dept
'IT'
>>> emp
('Ram', 24000, 'IT')
>>> name = 'Shyam'
>>> name
'Shyam'
>>> emp
('Ram', 24000, 'IT')
>>> emp_1 = emp
>>> emp_2
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    emp_2
NameError: name 'emp_2' is not defined
>>> emp_1
('Ram', 24000, 'IT')
>>> list(emp_1)
['Ram', 24000, 'IT']
>>> data = {"name":"Ram","sal":25000,"dept":"IT"}
>>> data
{'name': 'Ram', 'sal': 25000, 'dept': 'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["name"]
'Ram'
>>> data = {"names":['ram','shyam','gopal'],"sal":[45000,43000,25000],"dept":['IT','HR','Sales']}
>>> data
{'names': ['ram', 'shyam', 'gopal'], 'sal': [45000, 43000, 25000], 'dept': ['IT', 'HR', 'Sales']}
>>> for item in data:
	print(item)

	
names
sal
dept
>>> data.values()
dict_values([['ram', 'shyam', 'gopal'], [45000, 43000, 25000], ['IT', 'HR', 'Sales']])
>>> data.keys()
dict_keys(['names', 'sal', 'dept'])
>>> data.items()
dict_items([('names', ['ram', 'shyam', 'gopal']), ('sal', [45000, 43000, 25000]), ('dept', ['IT', 'HR', 'Sales'])])
>>> for item in data.items():
	print(item)

	
('names', ['ram', 'shyam', 'gopal'])
('sal', [45000, 43000, 25000])
('dept', ['IT', 'HR', 'Sales'])
>>> for item in data.values():
	print(item)

	
['ram', 'shyam', 'gopal']
[45000, 43000, 25000]
['IT', 'HR', 'Sales']
>>> 
