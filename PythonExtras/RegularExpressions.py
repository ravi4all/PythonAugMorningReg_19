Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> msg = "Hello Ram, Your Salary is 25000"
>>> re.findall('[a-z]\w+',msg)
['ello', 'am', 'our', 'alary', 'is']
>>> re.findall('[A-Z]\w+',msg)
['Hello', 'Ram', 'Your', 'Salary']
>>> re.findall('[S]\w+',msg)
['Salary']
>>> re.findall('[Sal]\w+',msg)
['llo', 'am', 'Salary']
>>> re.findall('(Sal)\w+',msg)
['Sal']
>>> re.findall('(S)\w+',msg)
['S']
>>> re.findall('([S])\w+',msg)
['S']
>>> re.findall('([S]\w+)',msg)
['Salary']
>>> re.findall('([Sa]\w+)',msg)
['am', 'Salary']
>>> re.findall('([S]\w+)',msg)
['Salary']
>>> re.findall('\d+',msg)
['25000']
>>> ids = ["ram@gmail.com","ram12@gmail.com","_ram@gmail.com","ram@@gmail.com","ram@gmail"]
>>> re.search('([a-z|0-9]\w+[@]\w+[.]\w{2,3})',ids[0])
<re.Match object; span=(0, 13), match='ram@gmail.com'>
>>> for item in ids:
	if re.search('([a-z|0-9]\w+[@]\w+[.]\w{2,3})',ids[0]):
		print(item)

		
ram@gmail.com
ram12@gmail.com
_ram@gmail.com
ram@@gmail.com
ram@gmail
>>> for item in ids:
	if re.match('([a-z|0-9]\w+[@]\w+[.]\w{2,3})',ids[0]):
		print(item)

		
ram@gmail.com
ram12@gmail.com
_ram@gmail.com
ram@@gmail.com
ram@gmail
>>> for item in ids:
	if re.match('([a-z|0-9]\w+[@]\w+[.]\w{2,3})',item):
		print(item)

		
ram@gmail.com
ram12@gmail.com
>>> 
