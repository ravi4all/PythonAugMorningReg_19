# file = open('file_2.txt','w')
# data = "hello this is file handling"

file = open('file_2.txt','a')
data = "this is another text"
file.write(data)
file.close()