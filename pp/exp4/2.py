# Reverse a string

str = input("Enter a string:\t")

# Iterate through the string in reverse order and print each character
for i in range(len(str) - 1, -1, -1):
    print(str[i], end="")


