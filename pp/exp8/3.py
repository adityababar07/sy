# fibonacci number series

def fibonacciSeries(n):
    if n <= 1:
        return n
    else:
        return fibonacciSeries(n-1)+fibonacciSeries(n-2)

n = int(input("enter the number of terms you want:\t"))

series = [fibonacciSeries(i) for i in range(n+1)]

print(f"the fibonacii series till {n}th term is :-\n")    

for i in series:
    print(i,end=", ")
print("\n")

'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp8/3.py
enter the number of terms you want:     8
the fibonacii series till 8th term is :-

0, 1, 1, 2, 3, 5, 8, 13, 21, 

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''    
