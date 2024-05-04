# shitting element to right as no. of times mentioned

def shiftElements(num):
    a = [1, 10, 5, 7, 2]

    b = [0, 0, 0, 0, 0]
    
    l = len(a)
    num -=1
    
    for i in range(len(a)):       
        l -=1
        b[num] = a[l]
        num -=1
    
    return b

print(f"after shifting elements {1} times to right result is :\t{shiftElements(1)}")

print(f"after shifting elements {2} times to right result is :\t{shiftElements(2)}")

'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp8/4.py
after shifting elements 1 times to right result is :    [2, 1, 10, 5, 7]
after shifting elements 2 times to right result is :    [7, 2, 1, 10, 5]
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''

