# CSV - Comma Seperated Values

import csv

# users = [
#     {"name":"Ram","age":21,"college":"IP","marks":76},
#     {"name":"Shyam","age":22,"college":"DU","marks":79},
#     {"name":"Gopal","age":20,"college":"IP","marks":56},
#     {"name":"Kunal","age":23,"college":"IP","marks":98},
# ]
#
# with open('users.csv','w', newline='') as file:
#     writer = csv.writer(file)
#     for user in users:
#         writer.writerow(user.values())

with open('users.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# import pandas as pd
# df = pd.read_csv('users.csv')
# print(df)