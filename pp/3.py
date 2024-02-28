# factorial of first 100 no.s

num = int(input("enter the number who's factorial you want :\t"))

sum = 1
for i in range(1, num+1):
    sum *= i

print(sum)
