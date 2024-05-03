dict1 = {"roll_no":1, "name":"aditya", "city":"miraj", "hometown":"cheruthony",}

# using print statement

print("dict1")

# using values method to print values

print("\n using values method to print values \n")
for i in dict1.values():
    print(i)

# using key value method

print("\nusing key value method\n")
for i,j in dict1.items():
    print(f"{i}:{j}") 

# using get method to access elements in dictionary

print("\nusing get method to access elements in dictionary\n")
print(dict1.get("roll_no"))

# adding elements into the dictionary

dict1["last_sem_status"] = "pass"
print(dict1)

# modifing the dictionary

dict1["city"] = "sangli"
print(dict1)

# deleting element in dictionary

dict1.pop("last_sem_status")
print(dict1)

# traversing through the dictionary

print("\ntraversing through dictionary")
for i in dict1.values():
    print(i)

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python pp/exp7/1.py
dict1

 using values method to print values 

1
aditya
miraj
cheruthony

using key value method

roll_no:1
name:aditya
city:miraj
hometown:cheruthony

using get method to access elements in dictionary

1
{'roll_no': 1, 'name': 'aditya', 'city': 'miraj', 'hometown': 'cheruthony', 'last_sem_status': 'pass'}
{'roll_no': 1, 'name': 'aditya', 'city': 'sangli', 'hometown': 'cheruthony', 'last_sem_status': 'pass'}
{'roll_no': 1, 'name': 'aditya', 'city': 'sangli', 'hometown': 'cheruthony'}

traversing through dictionary
1
aditya
sangli
cheruthony
'''
