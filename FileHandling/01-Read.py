file = open('file_1.txt','r')
# data = file.read()

# data = file.readline()

# data = file.readlines()

# data = file.read(10)

file.seek(10)
data = file.read()
print(data)
file.close()