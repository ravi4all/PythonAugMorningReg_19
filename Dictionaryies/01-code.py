students = [
    {'s_name':"Ram",'s_id':101,'s_hobby':'cricket','s_marks':[56,78,65]},
    {'s_name':"Aman",'s_id':102,'s_hobby':'hockey','s_marks':[54,79,51]},
    {'s_name':"Suman",'s_id':103,'s_hobby':'football','s_marks':[78,98,96]},
    {'s_name':"Kunal",'s_id':104,'s_hobby':'chess','s_marks':[91,71,60]},
    {'s_name':"Anuj",'s_id':105,'s_hobby':'cricket','s_marks':[43,48,51]},
    {'s_name':"Shyam",'s_id':106,'s_hobby':'chess','s_marks':[98,90,24]},
    ]

for student in students:
    if student['s_hobby'] == 'chess':
        print(student['s_name'],student['s_hobby'])

print("------------------")

print("Average Marks ----")
for student in students:
    marks = student['s_marks']
    avg = sum(marks) / len(marks)
    avg = round(avg,2)
    print("Average Marks of {} is {}".format(student['s_name'],avg))
