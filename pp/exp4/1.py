# Calculate the distance between corresponding characters of two strings

str1 = input("Enter a string:\t")
str2 = input("Enter a string:\t")
count = 0

# Check if the lengths of the strings are equal
if len(str1) != len(str2):
    print("-1")
    exit()

# Calculate the distance between corresponding characters
for i in range(len(str1)):
    count += abs(ord(str1[i]) - ord(str2[i]))

# Print the distance
print(f"The distance between the characters of the strings is {count}.")

'''
Output:-

Enter a string: cat
Enter a string: dog
The distance between the characters of the strings is 28.
'''
