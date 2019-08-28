import random
# def even(num):
#     return num % 2 == 0

# e = even(23)
# print(e)

numbers = [i for i in range(1,25)]

random.shuffle(numbers)

# e = []
# for n in numbers:
#     if even(n):
#         e.append(n)
#
# print(e)

e = list(filter(lambda n : n % 2 == 0, numbers))
print(e)