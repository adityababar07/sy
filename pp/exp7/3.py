grocery_items = {
    'apple': 150.0,
    'banana': 75.0,
    'orange': 110.0,
    'bread': 195.0,
    'milk': 130.0,
    'eggs': 120.0,
    'cheese': 250.0,
    'chicken': 300.0,
    'rice': 135.0,
    'pasta': 95.0
}

grocery_items_quantity = {
    'apple': 5,
    'banana': 3,
    'orange': 2,
    'bread': 2,
    'milk': 1,
    'eggs': 12,
    'cheese': 1,
    'chicken': 2,
    'rice': 3,
    'pasta': 2
}

print("heloo".center(100))

print('''
=============================================================
                       GROCERY BILL
=============================================================
''')

print('''\n
-------------------------------------------------------------
''')

print('''
Item           Quantity     Price (Rupees)     Total (Rupees)
''')

print('''\n
-------------------------------------------------------------
''')
for item,price in grocery_items.items():
    print(f'''
    {item}           {grocery_items_quantity[item]}    {price}     {grocery_items_quantity[item]*price}
    ''')

print('''\n
-------------------------------------------------------------
''')

print('''\n
-------------------------------------------------------------
''')

