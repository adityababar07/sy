# find out prime no. from first 100 no.s

num = 0

prime_no = [2, 3, 5, 7]

for i in range(2,101):
    num=i
    if num%2!=0 and num%3!=0 and num%5!=0 and num%7!=0:
        prime_no.append(num)

print(f"List of prime numbers in first 100 numbers is {prime_no}.")

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/10.py
List of prime numbers in first 100 numbers is [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].
'''
