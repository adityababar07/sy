# factorial of  no.

num = int(input("enter the number who's factorial you want :\t"))

factorial = 1
for i in range(1, num+1):
    factorial *= i

print(f"Factorial of the number is {factorial} ")
