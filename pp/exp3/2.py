# Calculate the sum of the first 50 even numbers

sum = 0
num = 0
num_50 = []

# Loop until the first 50 even numbers are found
while True:
    # Check if the list contains 50 numbers
    if len(num_50) == 50:
        # Calculate the sum of the first 50 even numbers
        for i in num_50:
            sum += i
        # Print the sum
        print(f"Sum of first 50 even numbers is {sum}.")
        # Exit the loop
        exit()

    num += 1

    # If the number is even, add it to the list
    if num % 2 == 0:
        num_50.append(num) 

'''
Output:-

Sum of first 50 even numbers is 2550.
'''
