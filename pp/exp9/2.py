# Basic calculator 

# Importing necessary modules
import sys
from pyfiglet import Figlet
from add import add
from substract import substract
from multiply import multiply
from division import division

# Appending the path of the package to the Python path using sys.path.append()
sys.path.append("/home/aditya/Code/sy/pp/exp9/calculator")

# Creating a Figlet object for styling text
f = Figlet(font='slant')
print(f.renderText('Basic calculator'))

print("============================================================")
print("\nNote:\nOnly enter one number at a time with the operator for the operation infront of the number!!!!\nTo quit the program, enter 'q' \n")

number = ""
result = 0

while number != "q":
    number = input("Enter the number:\t")
    try:
        if number[0] == '+':
            result = add(result, int(number[1:]))
            print(f"Result: {result}")
        elif number[0] == '-':
            result = substract(result, int(number[1:]))
            print(f"Result: {result}")
        elif number[0] == '*':
            result = multiply(result, int(number[1:]))
            print(f"Result: {result}")
        elif number[0] == '/':
            result = division(result, int(number[1:]))
            print(f"Result: {result}")
        elif number == "q":
            print("Exiting the program....")
            exit()
        else:
            print("Remember to enter the operator in front of the number, and enter only one number at a time!!!!!!")
    except Exception as error:
        print("It seems you entered a wrong input!!!!!\nRemember to enter the operator in front of the number, and enter only one number at a time!!!!!!")
        print("\nThe error is :\t", error)


'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp-/pp/exp9 (master) $ tree
.
├── 1_main.py
├── 2.py
├── calculator
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── add.cpython-311.pyc
│   │   ├── division.cpython-311.pyc
│   │   ├── multiply.cpython-311.pyc
│   │   └── substract.cpython-311.pyc
│   ├── add.py
│   ├── division.py
│   ├── multiply.py
│   └── substract.py
└── module_1.py

2 directories, 12 files

(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp9/2.py
    ____             _                    __           __      __            
   / __ )____ ______(_)____   _________ _/ /______  __/ /___ _/ /_____  _____
  / __  / __ `/ ___/ / ___/  / ___/ __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / /_/ / /_/ (__  ) / /__   / /__/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_____/\__,_/____/_/\___/   \___/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
                                                                             

============================================================

Note:
Only enter one number at a time with the operator for the operation infront of the number!!!!
To quite the program enter 'q' 

enter the number:       +50
Result: 50
enter the number:       -20
Result: 30
enter the number:       *2
Result: 60
enter the number:       /30
Result: 2.0
enter the number:       *7894
Result: 15788.0
enter the number:       +58
Result: 15846.0
enter the number:       +97
Result: 15943.0
enter the number:       +452255
Result: 468198.0
enter the number:       *78855617525
Result: 3.692004241396995e+16
enter the number:       -745585
Result: 3.692004241322437e+16
enter the number:       /7466845
Result: 4944530442.673494
enter the number:       54
Remember to enter the operator infront of the number also enter only one number at a time!!!!!!
enter the number:       +rfg
It seems you entered a wrong input!!!!!
Remember to enter the operator infront of the number also enter only one number at a time!!!!!!

The error is :   invalid literal for int() with base 10: 'rfg'
enter the number:       gg
Remember to enter the operator infront of the number also enter only one number at a time!!!!!!
enter the number:       q
Exiting the program....
(sy) ┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''

