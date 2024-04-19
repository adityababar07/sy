# Calculate the sum of the first 50 odd numbers

sum = 0
num = 0
num_50 = []

# Loop until the first 50 odd numbers are found
while True:
    # Check if the list contains 50 numbers
    if len(num_50) == 50:
        # Calculate the sum of the first 50 odd numbers
        for i in num_50:
            sum += i
        # Print the sum
        print(f"Sum of first 50 odd numbers is {sum}.")
        # Exit the loop
        exit()

    num += 1

    # If the number is odd, add it to the list
    if num % 2 != 0:
        num_50.append(num) 

'''
Output:-

Sum of first 50 odd numbers is 2500.
'''
