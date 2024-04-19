# fibonacci using recursive function

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms you want in Fibonacci series:\t"))
series = [fibonacci(i) for i in range(n)]
print(series)