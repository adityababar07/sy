# Find prime numbers from the first 100 numbers

# Initialize a list with known prime numbers
prime_no = [2, 3, 5, 7]

# Iterate through numbers from 2 to 100
for num in range(2, 101):
    # Check if the number is divisible by any known prime numbers
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
        # If not divisible, add it to the list of prime numbers
        prime_no.append(num)

# Print the list of prime numbers
print(f"List of prime numbers in the first 100 numbers is {prime_no}.")

'''
Output:-

List of prime numbers in the first 100 numbers is [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].
'''
