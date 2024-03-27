# finding the distance between two characters in a string

str1 = input("enter a string:\t")
str2 = input("enter a string:\t")
count = 0

if len(str1) != len(str2):
    exit()

for i in range(len(str1)):
    count += abs(ord(str1[i])-ord(str2[i]))

print(f"the distance between the characters of the string is {count}.")
