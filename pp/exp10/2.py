string = "abcdefghijklmnopqrstuvwxyz"

# Write the string into a file
with open("file2.txt", "w") as file:
    file.write(string)

# Read the contents of the file, reverse them, and print as a list
with open("file2.txt", "r") as file:
    output = list(file.read())
    output.reverse()
    output = "".join(output)
    print(output)


'''
output:-

(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $python 2.py
zyxwvutsrqponmlkjihgfedcba
(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $
'''
