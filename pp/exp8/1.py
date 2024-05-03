# required arguments
print("requires arguments:-\n")

# Defining a function with required arguments 'name' and 'age'
def studentDetail(name, age):
    print("Name:", name)
    print("Age:", age)
    
# Calling the function with required arguments
studentDetail("Aditya", 21)

# keyword arguments
print("\nkeyword arguments:-\n")

# Defining a function with required arguments 'name' and 'age'
def studentDetail(name, age):
    print("Name:", name)
    print("Age:", age)
    
# Calling the function with keyword arguments
studentDetail(age = 21, name = "Aditya")

# default arguments
print("\ndefault arguments:-\n")

# Defining a function with default argument 'age' set to 21
def studentDetail(name, age = 21):
    print("Name:", name)
    print("Age:", age)
    
# Calling the function with only one argument, using the default value for 'age'
studentDetail("Aditya")

# variable-length arguments
print("\nvariable-length arguments:-\n")

# Defining a function with variable-length arguments 'names'
def studentDetail(*names):
    # Iterating over each name in the variable-length arguments
    for name in names:
        print("Name:", name)
        
# Calling the function with variable number of arguments
studentDetail("Aditya", "Atul", "Rohan")

# keyword variable-length arguments
print("\nkeyword variable-length arguments:-\n")

# Defining a function with keyword variable-length arguments 'details'
def studentDetail(**details):
    # Iterating over each key-value pair in the keyword variable-length arguments
    for key, value in details.items():
        print(f"{key}: {value}")

# Calling the function with keyword variable-length arguments
studentDetail(name = "Aditya", age = 21, course = "IT")

# Output:-

'''
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp8/1.py
requires arguments:-

Name: Aditya
Age: 21

keyword arguments:-

Name: Aditya
Age: 21

default arguments:-

Name: Aditya
Age: 21

variable-length arguments:-

Name: Aditya
Name: Atul
Name: Rohan

keyword variable-length arguments:-

name: Aditya
age: 21
course: IT
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
