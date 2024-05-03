# Importing the 'randint' function from the 'random' module
from random import randint as rd

# Initializing an empty list to store random numbers
a = []

# Generating a list of 20 random integers between -999 and 999
for i in range(20):
    # Generating a random integer and appending it to the list 'a'
    num = rd(-999, 999)
    a.append(num)

# Initializing empty lists to store odd, even, negative, and prime numbers
odd = []
even = []
negative = []
prime_no = []

# Iterating through each number in the list 'a' to categorize them
for i in a:
    # Checking if the number is odd
    if i % 2 != 0:
        odd.append(i)  # Appending odd numbers to the 'odd' list
    
    else:
        even.append(i)  # Appending even numbers to the 'even' list

# Iterating through each number in the list 'a' to find negative numbers
for i in a:
    if i < 0:
        negative.append(i)  # Appending negative numbers to the 'negative' list

# Iterating through each number in the list 'a' to find prime numbers
for i in a:
    # Checking if the number is prime
    if i in [2, 3, 5, 7] or (i > 0 and i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        prime_no.append(i)  # Appending prime numbers to the 'prime_no' list

# Printing the original list of numbers 'a'
print("original list of numbers is", a, "\n")

# Printing the list of odd numbers and its length
print(f"list of odd numbers is {odd}.\n The length of the list is {len(odd)}.\n")

# Printing the list of even numbers and its length
print(f"list of even numbers is {even}.\n The length of the list is {len(even)}.\n")

# Printing the list of negative numbers and its length
print(f"list of negative numbers is {negative}.\n The length of the list is {len(negative)}.\n")

# Printing the list of prime numbers and its length
print(f"list of prime numbers is {prime_no}.\n The length of the list is {len(prime_no)}.\n")

'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp5/4.py
original list of numbers is [-357, 895, -583, -501, -12, 532, -175, -849, -205, 172, -159, 133, -6, -71, 689, -129, 478, -787, 642, 224] 

list of odd numbers is [-357, 895, -583, -501, -175, -849, -205, -159, 133, -71, 689, -129, -787].
 The length of the list is 13.

list of even numbers is [-12, 532, 172, -6, 478, 642, 224].
 The length of the list is 7.

list of negative numbers is [-357, -583, -501, -12, -175, -849, -205, -159, -6, -71, -129, -787].
 The length of the list is 12.

list of prime numbers is [689].
 The length of the list is 1.

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
