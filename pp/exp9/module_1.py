# module
# f1 ->  factorial of given number
# f2 -> finding the largest of three numbers
# f3 -> add first 100 natural numbers 

# f1: Calculate the factorial of a given number
def f1(num):
    if num < 1:
        return 1
    else:
        return num * f1(num - 1)

# f2: Find the largest of three numbers
def f2(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

# f3: Add the first 100 natural numbers
def f3():
    num = 1
    sum = 0
    while num < 101:
        sum += num
        num += 1
    return sum
