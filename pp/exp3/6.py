# Find the largest and smallest of three numbers

num1 = int(input("Enter a number:\t"))
num2 = int(input("Enter a number:\t"))
num3 = int(input("Enter a number:\t"))

# Comparing the numbers to find the largest and smallest
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1} is the largest and {num3} is the smallest.")
    else:
        print(f"{num1} is the largest and {num2} is the smallest.")
        
elif num2 > num3 and num2 > num1:
    if num3 > num1:
        print(f"{num2} is the largest and {num1} is the smallest.")
    else:
        print(f"{num2} is the largest and {num3} is the smallest.")
        
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(f"{num3} is the largest and {num2} is the smallest.")
    else:
        print(f"{num3} is the largest and {num1} is the smallest.")

'''
Output:-

enter a number: 75
enter a number: 45
enter a number: 85
85 is the largest and 45 is the smallest.
'''
