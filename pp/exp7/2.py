# creating a dictionary of students and inputing data of 5 students from user

students = {}

for i in range(5):
    print('\n')
    roll_no = input("enter the roll number of the student:\t")
    name = input("enter the name of the student:\t")
    course = input("enter the course enrolled by the student:\t")
    semester = input("enter the semester:\t")
    science = input("enter the marks obtained in science:\t")
    maths = input("enter the marks obtained in maths:\t")
    english = input("enter the marks obtained in english:\t")
    hindi = input("enter the marks obtained in hindi:\t")
    social = input("enter the marks obtained in social:\t")

    students[roll_no] = {}
    students[roll_no]["name"] = name
    students[roll_no]["course"] = course
    students[roll_no]["semester"] = semester
    students[roll_no]["science"] = science
    students[roll_no]["maths"] = maths
    students[roll_no]["english"] = english
    students[roll_no]["hindi"] = hindi
    students[roll_no]["social"] = social


# printing the students dictionary

print('\n',students)

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/exp7/2.py

enter the roll number of the student:   63
enter the name of the student:  atul shivaling wale
enter the course enrolled by the student:       engg
enter the semester:     4
enter the marks obtained in science:    70
enter the marks obtained in maths:      75
enter the marks obtained in english:    70
enter the marks obtained in hindi:      90
enter the marks obtained in social:     95

enter the roll number of the student:   1
enter the name of the student:  aditya sambhaji babar
enter the course enrolled by the student:       IT
enter the semester:     3
enter the marks obtained in science:    80
enter the marks obtained in maths:      90
enter the marks obtained in english:    95
enter the marks obtained in hindi:      75
enter the marks obtained in social:     90

enter the roll number of the student:   11
enter the name of the student:  rohan subhash fasale
enter the course enrolled by the student:       cse
enter the semester:     5
enter the marks obtained in science:    80
enter the marks obtained in maths:      56
enter the marks obtained in english:    76
enter the marks obtained in hindi:      89
enter the marks obtained in social:     80

enter the roll number of the student:   16
enter the name of the student:  ashish balkrishn katkar
enter the course enrolled by the student:       aids
enter the semester:     3
enter the marks obtained in science:    70
enter the marks obtained in maths:      78
enter the marks obtained in english:    98
enter the marks obtained in hindi:      65
enter the marks obtained in social:     74

enter the roll number of the student:   27
enter the name of the student:  aditi raju sabne
enter the course enrolled by the student:       ecs
enter the semester:     4
enter the marks obtained in science:    67
enter the marks obtained in maths:      76
enter the marks obtained in english:    80
enter the marks obtained in hindi:      87
enter the marks obtained in social:     88

{'63': {'name': 'atul shivaling wale', 'course': 'engg', 'semester': '4', 'science': '70', 'maths': '75', 'english': '70', 'hindi': '90', 'social': '95'}, '1': {'name': 'aditya sambhaji babar', 'course': 'IT', 'semester': '3', 'science': '80', 'maths': '90', 'english': '95', 'hindi': '75', 'social': '90'}, '11': {'name': 'rohan subhash fasale', 'course': 'cse', 'semester': '5', 'science': '80', 'maths': '56', 'english': '76', 'hindi': '89', 'social': '80'}, '16': {'name': 'ashish balkrishn katkar', 'course': 'aids', 'semester': '3', 'science': '70', 'maths': '78', 'english': '98', 'hindi': '65', 'social': '74'}, '27': {'name': 'aditi raju sabne', 'course': 'ecs', 'semester': '4', 'science': '67', 'maths': '76', 'english': '80', 'hindi': '87', 'social': '88'}}
@adityababar07 ➜ /workspaces/sy-pp- (master) $ 
'''
