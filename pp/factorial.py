# factorial of  no.

num = int(input("enter the number who's factorial you want :\t"))

factorial = 1
for i in range(1, num+1):
    factorial *= i

print(f"Factorial of the number is {factorial} ")


'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/factorial.py
enter the number who's factorial you want :     26
Factorial of the number is 403291461126605635584000000 
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''