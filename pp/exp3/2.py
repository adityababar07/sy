# sum 0f first 50 even no.

sum = 0
num = 0

num_50 = []

while True:
    if len(num_50) == 50:
        for i in num_50:
            sum += i
        print(f"Sum of first 50 even no.s is {sum}.")
        exit()

    num += 1

    if num % 2 == 0:
        num_50.append(num) 

'''
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/5.py
Sum of first 50 even no.s is 2550.
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
