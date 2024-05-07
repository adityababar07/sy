string = "abcdefghijklmnopqrstuvwxyz"

# Write the string into a file
with open("file2.txt", "w") as file:
    file.write(string)

# Read the contents of the file, reverse them, and print as a list
with open("file2.txt", "r") as file:
    output = list(file.read())
    output.reverse()
    print(output)


'''
output:-

(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $python 2.py
['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $
'''
