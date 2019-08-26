# def add(*x):
#     print(x)
#
#     sum = 0
#     for i in x:
#         sum += i
#
#     print(sum)
#
# add(4,5,6,3,5,)
# add(3,5)
# add(5,7,6,3,3,4,65,7)

def student(id,*marks,name=""):
    print("Id :",id)
    print("Name :",name)
    print("Marks :",marks)

student(101,67,56,86,23,name='Ram')
student(102,54,58,87,name='Shyam')