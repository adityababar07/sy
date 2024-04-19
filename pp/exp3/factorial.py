# Calculate the factorial of a number

num = int(input("Enter the number whose factorial you want:\t"))

# Initialize factorial to 1
factorial = 1

# Calculate the factorial using a loop
for i in range(1, num + 1):
    factorial *= i

# Print the factorial
print(f"Factorial of the number is {factorial} ")

'''
Output:-

enter the number who's factorial you want :     26
Factorial of the number is 403291461126605635584000000 
'''
