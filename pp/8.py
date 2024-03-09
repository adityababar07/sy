# seperation and addition of digits of a given no.

number = int(input("enter the number:\t"))
sum=0

while True:
    sum+=(number%10)
    number//=10
    if number == 0:
        break 

print(f"\nsum of the digits is {sum}.")

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/8.py
enter the number:       1234

sum of the digits is 10.
'''