# Separate and add the digits of a given number

number = int(input("Enter the number:\t"))
sum = 0

# Iterate through each digit of the number
while True:
    # Extract the last digit of the number and add it to the sum
    sum += (number % 10)
    # Remove the last digit from the number
    number //= 10
    # Break the loop when all digits have been processed
    if number == 0:
        break 

# Print the sum of the digits
print(f"\nSum of the digits is {sum}.")

'''
Output:-

enter the number:       1234

sum of the digits is 10.
'''
