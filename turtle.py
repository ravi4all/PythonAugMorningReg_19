Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Pen()
>>> t.shape("turtle")
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.forward(200)
>>> t.left(90)
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)

	
>>> t.reset()
>>> for i in range(4):
	t.forward(200)
	t.left(90)
	print(i)

	
0
1
2
3
>>> t.reset()
>>> for i in range(40):
	t.forward(4*i)
	t.left(90)

	
>>> t.reset()
>>> for i in range(20):
	t.circle(5*i)
	t.left(90)

	
>>> t.reset()
>>> t.speed(0)
>>> for i in range(200):
	t.circle(5*i)
	t.left(90)

	
>>> 
