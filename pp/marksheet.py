# grade of student

marks = []

subjects = ['english', 'maths', 'science', 'social', 'hindi']

for subject in subjects:
    mark = int(input(f"enter the marks obtained  in {subject}:\t"))
    marks.append(mark)

percentage = (sum(marks)/500)*100

print(f"Percentage of the student is {percentage}")

if percentage >=90:
    grade = "A"
elif percentage >=80:
    grade = "B"
elif percentage >=70:
    grade = "C"
elif percentage >=60:
    grade = "D"
elif percentage >=50:
    grade = "E"
else:
    grade = "F"

print(f"The grade of the student is {grade}.")

failed_sub = 0
for mark in marks:
    if mark<40:
        failed_sub +=2 

if grade == "F" or failed_sub>0:
    print("Student has failed.")


'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/marksheet.py
enter the marks obtained  in english:   48
enter the marks obtained  in maths:     75
enter the marks obtained  in science:   95
enter the marks obtained  in social:    48
enter the marks obtained  in hindi:     75
Percentage of the student is 68.2
The grade of the student is D.
'''