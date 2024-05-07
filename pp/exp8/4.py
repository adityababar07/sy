# Define a function to shift elements to the right by a specified number of times
def shiftElements(num):
    # Original list
    a = [1, 10, 5, 7, 2]

    # Initialize a new list to store shifted elements
    b = [0, 0, 0, 0, 0]
    
    # Get the length of the original list
    l = len(a)
    num -= 1
    
    # Iterate through the elements of the original list
    for i in range(len(a)):       
        l -= 1
        # Shift the element to the right by the specified number of times
        b[num] = a[l]
        num -= 1
    
    # Return the shifted list
    return b

# Test the function with different number of shifts
print(f"after shifting elements {1} times to the right result is :\t{shiftElements(1)}")
print(f"after shifting elements {2} times to the right result is :\t{shiftElements(2)}")

'''
Output:-

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp8/4.py
after shifting elements 1 times to right result is :    [2, 1, 10, 5, 7]
after shifting elements 2 times to right result is :    [7, 2, 1, 10, 5]
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''

