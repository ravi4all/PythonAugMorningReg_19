# num = int(input("Enter a number : "))
#
# prime = True
#
# for i in range(2,num):
#     if num % i == 0:
#         # print("Not Prime")
#         prime = False
#         break
#     else:
#         # print("Prime Number")
#         prime = True
#
# if prime:
#     print("Prime Number")
# else:
#     print("Not Prime")


num = int(input("Enter a number : "))

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")