string = "Hello, how are you?"

list1 = ["Hello", "how", "are", "you?"]

# Write contents into a file
with open("file1.txt", "w") as file:
    file.write(string)

# Read and print the contents of the file
with open("file1.txt", "r") as file:
    print(file.read())

# Overwrite the contents of the file with the list items
with open("file1.txt", "w") as file:
    file.writelines(list1)

# Read and print the first line of the file
with open("file1.txt", "r") as file:
    print(file.readline())

# Read and print all lines of the file as a list
with open("file1.txt", "r") as file:
    print(file.readlines())

# Append contents into a file
with open("file1.txt", "a") as file:
    file.write("\nI am fine.")

# Read and print the contents of the file
with open("file1.txt", "r") as file:
    print(file.read())

# Read and print the first line of the file
with open("file1.txt", "r") as file:
    print(file.readline())

# Read and print all lines of the file as a list
with open("file1.txt", "r") as file:
    print(file.readlines())

'''
Output:

(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $python 1.py
Hello, how are you?
Hellohowareyou?
['Hellohowareyou?']
Hellohowareyou?
I am fine.
Hellohowareyou?

['Hellohowareyou?\n', 'I am fine.']
(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy/pp/exp10]
└──╼ $
'''
