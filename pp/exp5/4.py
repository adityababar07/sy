#
from random import randint as rd

a = []

<<<<<<< HEAD
a.append(randint)
=======
# Generate a list of 20 random integers between 10 and 100
for i in range(20):
    num = rd(-999, 999)
    a.append(num)

odd = []
even = []
negative = []
prime_no = []

for i in a:
    if i % 2 == 0:
        even.append(i)
    elif i%2 != 0:
        odd.append(i)

for i in a:
    if i<0:
        negative.append(i)

for i in a:
    if i in [2, 3, 5, 7] or i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 and i>0:
        prime_no.append(i)

print("original list of numbrs is {a}\n")

print(f"list of odd numbers is {odd}.\n The length of the list is {len(odd)}.\n")

print(f"list of even numbers is {even}.\n The length of the list is {len(even)}.\n")

print(f"list of negative numbers is {negative}.\n The length of the list is {len(negative)}.\n")

print(f"list of odd numbers is {prime_no}.\n The length of the list is {len(prime_no)}.\n")

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python3 pp/exp5/4.py
original list of numbrs is {a}

list of odd numbers is [401, -961, -945, -835, -749, 237, -259, 715, 717, -3, -543, -745, 3].
 The length of the list is 13.

list of even numbers is [90, 738, 834, -328, 674, 40, 936].
 The length of the list is 7.

list of negative numbers is [-961, -945, -835, -749, -328, -259, -3, -543, -745].
 The length of the list is 9.

list of odd numbers is [401, 3].
 The length of the list is 2.

@adityababar07 ➜ /workspaces/sy-pp- (master) $ 
'''
>>>>>>> b836be55164d509915994772293c27e4a9ace8da
