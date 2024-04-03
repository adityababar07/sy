# string concatination

str1 = "hello"
str2 = "world!!!"

str3 = str1 +" "+ str2

print(str3)

# string appending

str1+= str2
print(str1)


#string indexing

print(f"index of l is {str1.index('l')}")



str = "Hello, how are you?"


# slicing a string

print(str[::2] ,str[:4], str[3:8], str[5:], str[5:9:3])


# string methods

# upper , lower and title case

print(f"the string in upper case:- {str.upper()}\n")

print(f"the string in lower case:- {str.lower()}\n")

print(f"the string in title case:- {str.title()}\n")

print(f"the string in ends with:- {str.endswith('x')}\n")

print(f"the string in starts with:- {str.startswith('H')}\n")

print(f"finding how  in string:- {str.find('how')}\n")

print(f"finding count of how  in string:- {str.count('how')}\n")

# split a string

print(str.split())


print(f"finding whether string is alphanumeric:- {str.isalnum()}\n")

print(f"finding whether string is alphabetic:- {str.isalpha()}\n")


'''
Output:-

┌─[✗]─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp4/3.py
hello world!!!
helloworld!!!
index of l is 2
Hlo o r o? Hell lo, h , how are you? ,o
the string in upper case:- HELLO, HOW ARE YOU?

the string in lower case:- hello, how are you?

the string in title case:- Hello, How Are You?

the string in ends with:- False

the string in starts with:- True

finding how  in string:- 7

finding count of how  in string:- 1

['Hello,', 'how', 'are', 'you?']
finding whether string is alphanumeric:- False

finding whether string is alphabetic:- False

┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $

'''


