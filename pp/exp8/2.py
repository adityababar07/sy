# Taking input from the user for the number whose factorial is to be calculated
num = int(input("enter the number whose factorial you want:\t"))

# Iterative function to calculate factorial
def factorial(num):
    factorial = 1
    
    # Looping from 'num' down to 1 and multiplying to calculate factorial
    while num > 0:
        factorial *= num
        num -= 1

    return factorial

# Printing the factorial using iterative function
print(f"The factorial of {num} using iterative function is {factorial(num)}")

# Recursive function to calculate factorial
def factorial0(num):
    # Base case: factorial of 0 or negative number is 1
    if num < 1:
        return 1
    # Recursive case: multiply the number with factorial of (number - 1)
    else:
        return num * factorial0(num - 1)

# Printing the factorial using recursive function
print(f"The factorial of {num} using recursive function is {factorial0(num)}")

'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp8/2.py
enter the number whose factorial you want:      5
The factorial of 5 using iterative function is 120
The factorial of 5 using recursive function is 120
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
