# find out largest and smallest of three no.s

num1 = int(input("enter a number:\t"))
num2 = int(input("enter a number:\t"))
num3 = int(input("enter a number:\t"))

if num1 >num2 and num2 >num3:
    print(f"{num1} is the largest and {num3} is the smallest.")
elif num2 >num3 and num3 >num1:
    print(f"{num2} is the largest and {num1} is the smallest.")
elif num3 >num1 and num1 >num2:
    print(f"{num3} is the largest and {num2} is the smallest.")

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/9.py
enter a number: 75
enter a number: 45
enter a number: 85
85 is the largest and 45 is the smallest.
'''
