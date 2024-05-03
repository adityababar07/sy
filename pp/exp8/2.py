# factorial of a no. using functions

num = int(input("enter the number whose factorial you want:\t"))
# iterative function

def factorial(num):
    factorial = 1
    
    while num > 0:
        factorial *= num
        num -= 1

    return factorial

print(f"The factorial of {num} using iterative function is {factorial(num)}")

# recursive function

def factorial0(num):
    if num<1:
        return 1
    else:
        return num*factorial(num-1)

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
