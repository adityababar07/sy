# importing functions f1, f2, f3 from module 1(module)
from module_1 import f1, f2, f3 

# factorial of given number
num = int(input("Enter the number:\t"))
print(f"Factorial of {num} is :\t{f1(num)}")

# finding the largest of three numbers
n1 = int(input("Enter a number:\t"))
n2 = int(input("Enter a number:\t"))
n3 = int(input("Enter a number:\t"))

print(f"Largest of the above entered three numbers is {f2(n1, n2, n3)}")

# add first 100 natural numbers
print(f"Sum after adding the first 100 natural numbers is {f3()}")

'''
Output:-
┌─[✗]─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp9/1_main.py
Enter the number:       5
Factorial of 5 is :     120
Enter a number: 45
Enter a number: 54
Enter a number: 75
Largest of the above entered three numbers is 75
Sum after adding the first 100 natural numbers is 5050
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
