# Calculate the grade of a student based on their marks

marks = []
subjects = ['English', 'Maths', 'Science', 'Social', 'Hindi']

# Input marks for each subject
for subject in subjects:
    mark = int(input(f"Enter the marks obtained in {subject}:\t"))
    marks.append(mark)

# Calculate the percentage
percentage = (sum(marks) / 500) * 100
print(f"Percentage of the student is {percentage}")

# Determine the grade based on the percentage
if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
elif percentage >= 50:
    grade = "E"
else:
    grade = "F"

print(f"The grade of the student is {grade}.")

# Check if the student has failed in any subject
failed_sub = 0
for mark in marks:
    if mark < 40:
        failed_sub += 2 

if grade == "F" or failed_sub > 0:
    print("Student has failed.")

'''
Output:-

Enter the marks obtained in English: 48
Enter the marks obtained in Maths: 75
Enter the marks obtained in Science: 95
Enter the marks obtained in Social: 48
Enter the marks obtained in Hindi: 75
Percentage of the student is 68.2
The grade of the student is D.
'''
