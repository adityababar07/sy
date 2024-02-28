# sum 0f first 100 odd no.

sum = 0
num = 0

num_100 = []

while True:
    if len(num_100) == 100:
        for i in num_100:
            sum += i
        print(sum)
        exit()

    num += 1

    if num % 2 != 0:
        num_100.append(num) 
