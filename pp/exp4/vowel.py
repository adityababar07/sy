# Finding the number of vowels, whitespaces, full stops, semicolons, and commas in a text

text = input("Enter the text:\t")
text = text.lower()

# Initialize counters for vowels and other characters
no_of_a = 0
no_of_o = 0
no_of_e = 0
no_of_i = 0
no_of_u = 0
no_of_vowels = 0
no_of_whitespaces = 0
no_of_fullstops = 0
no_of_semicolons = 0
no_of_commas = 0

# Iterate through each character in the text
for letter in text:
    if letter == 'a':
        no_of_a += 1
    elif letter == 'e':
        no_of_e += 1
    elif letter == 'i':
        no_of_i += 1
    elif letter == 'o':
        no_of_o += 1
    elif letter == 'u':
        no_of_u += 1
    elif letter == " ":
        no_of_whitespaces += 1
    elif letter == ".":
        no_of_fullstops += 1
    elif letter == ";":
        no_of_semicolons += 1
    elif letter == ",":
        no_of_commas += 1

# Calculate the total number of vowels
no_of_vowels = no_of_a + no_of_e + no_of_i + no_of_o + no_of_u

# Print the results
print(f"\nThe total number of vowels is {no_of_vowels},\nthe number of 'a' is {no_of_a},\nthe number of 'e' is {no_of_e},\nthe number of 'i' is {no_of_i},\nthe number of 'o' is {no_of_o},\nthe number of 'u' is {no_of_u},\nthe number of whitespaces is {no_of_whitespaces},\nthe number of semicolons is {no_of_semicolons},\nthe number of full stops is {no_of_fullstops}, and\nthe number of commas is {no_of_commas}.")

'''
Output:-

The total number of vowels is 98,
the number of 'a' is 19,
the number of 'e' is 27,
the number of 'i' is 26,
the number of 'o' is 18,
the number of 'u' is 8,
the number of whitespaces is 48,
the number of semicolons is 0,
the number of full stops is 2, and
the number of commas is 2.
'''
