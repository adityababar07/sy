# String concatenation

str1 = "hello"
str2 = "world!!!"
str3 = str1 + " " + str2
print(str3)

# String appending
str1 += str2
print(str1)

# String indexing
print(f"Index of 'l' is {str1.index('l')}")

# Slicing a string
str = "Hello, how are you?"
print(str[::2], str[:4], str[3:8], str[5:], str[5:9:3])

# String methods
# Upper, lower, and title case
print(f"The string in upper case: {str.upper()}")
print(f"The string in lower case: {str.lower()}")
print(f"The string in title case: {str.title()}")

# Endswith and Startswith
print(f"The string ends with 'x': {str.endswith('x')}")
print(f"The string starts with 'H': {str.startswith('H')}")

# Find and Count
print(f"Index of 'how' in string: {str.find('how')}")
print(f"Count of 'how' in string: {str.count('how')}")

# Split a string
print(str.split())

# isalnum and isalpha
print(f"The string is alphanumeric: {str.isalnum()}")
print(f"The string is alphabetic: {str.isalpha()}")

'''
Output:-

hello world!!!
helloworld!!!
Index of 'l' is 2
Hlo o r o? Hell lo, h , how are you? ,o
The string in upper case: HELLO, HOW ARE YOU?
The string in lower case: hello, how are you?
The string in title case: Hello, How Are You?
The string ends with 'x': False
The string starts with 'H': True
Index of 'how' in string: 7
Count of 'how' in string: 1
['Hello,', 'how', 'are', 'you?']
The string is alphanumeric: False
The string is alphabetic: False
'''
