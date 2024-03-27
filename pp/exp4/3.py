# string functions

# split a string

str = "Hello, how are you?"

print(str.split())

# string concatination

str1 = "hello"
str2 = "world!!!"

str3 = str1 +" "+ str2

print(str3)

# upper , lower and title case

print(f"the string in upper case:- {str.upper()}\n")

print(f"the string in lower case:- {str.lower()}\n")

print(f"the string in title case:- {str.title()}\n")

# slicing a string

print(str[::2] ,str[:4], str[3:8], str[5:], str[5:9:3])
