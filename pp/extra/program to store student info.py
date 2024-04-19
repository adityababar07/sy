# program to store student info in dictionary

stu_info = {1:{'name':'aditya','age':21,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'pass'}, 
            2:{'name':'tejas','age':20,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'pass'},
            3:{'name':'unmesh','age':21,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'pass'},
            4:{'name':'sanket','age':21,'class':'sy', 'fees': 10000, 'branch':'AIDS', 'last_year_status': 'fail'},
            5:{'name':'veer','age':20,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'ATKT'},
            6:{'name':'vijay','age':20,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'ATKT'},
            7:{'name':'om','age':21,'class':'sy', 'fees': 10000, 'branch':'AIDS', 'last_year_status': 'pass'},
            8:{'name':'Atul','age':21,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'pass'},
            9:{'name':'saurabh','age':21,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'fail'},
            10:{'name':'veena','age':20,'class':'sy', 'fees': 10000, 'branch':'ecs', 'last_year_status': 'pass'}}

for i in stu_info:
    print(f"student with roll no. {i} info:-")
    for j in stu_info[i]:
        print(f"{j} : {stu_info[i][j]}")
    print("\n")
    