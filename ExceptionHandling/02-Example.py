try:
    file = open('file_1.txt','w')
    data = "This is exception handling example"
    data = file.read()
except BaseException as ex:
    print(ex)
else:
    print(data)
finally:
    print("I will always execute")
    file.close()