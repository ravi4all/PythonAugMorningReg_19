file = open('image_11.jpg','rb')
data = file.read()
# print(data)
file.close()

file = open('image_22.jpg','wb')
file.write(data)
file.close()