from random import randint as rd

a = []

# Generate a list of 20 random integers between 10 and 100
for i in range(20):
    num = rd(10, 100)
    a.append(num)

# Sort the list in ascending order
a.sort()
print(a)

# Filter out numbers greater than 20 and less than 50 from the list
# (Note: Commented out due to issues in proper functioning of the program)
# for i in a:
#     if i > 20 and i < 50:
#         a.remove(i)

'''
output of above code:-
[15, 18, 21, 23, 24, 31, 35, 39, 42, 50, 51, 66, 75, 79, 82, 84, 89, 91, 93, 98]
[15, 18, 23, 31, 39, 50, 51, 66, 75, 79, 82, 84, 89, 91, 93, 98]
'''

# Create an empty list to store filtered numbers
b = []

# Iterate through the list 'a' and filter out numbers greater than 20 and less than 50
for i in a:
    if i > 20 and i < 50:
        pass
    else:
        b.append(i)

# Assign the filtered list back to 'a'
a = b
print(a)

'''
output:-
[16, 17, 18, 21, 28, 33, 40, 44, 45, 46, 50, 54, 56, 59, 72, 76, 91, 94, 97, 100]
[16, 17, 18, 50, 54, 56, 59, 72, 76, 91, 94, 97, 100]
'''
