students = {
    "names" : ["Shyam","Ram","Laxman","Kunal","Aman","Deepak"],
    "hobby" : ['Football','Cricket','Football','Cricket','Cricket','Football'],
    "grade" : ['A','A+','B','B+','A','A+'],
    "address" : ['Rohini','Rithala','Kohat','Rohini','Rithala','Rohini'],
    "marks" : [87,67,88,89,65,34]
    }

grades = students["grade"]
for i in range(len(grades)):
    if grades[i] == 'A+':
        print(students['names'][i],students['grade'][i])
