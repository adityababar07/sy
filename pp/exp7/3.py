# Dictionary containing prices of grocery items
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

# Dictionary containing quantities of grocery items
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

# Initializing total bill amount
total = 0

# Printing the bill header
print('''
=============================================================
                       GROCERY BILL
=============================================================

-------------------------------------------------------------
Item           Quantity     Price (Rupees)     Total (Rupees)
-------------------------------------------------------------
''')

# Iterating over each item and its price from the dictionary
for item, price in grocery_items.items():
    # Calculating total price for each item based on quantity
    item_total = grocery_items_quantity[item] * price
    # Printing item details and total price for the item
    print(f'''{item:<8}           {grocery_items_quantity[item]:<10}    {price:<12}     {item_total:<10}''')
    # Adding item total to the overall total bill amount
    total += item_total

# Printing the total bill amount
print(f'''
-------------------------------------------------------------
Total:                                           ₹ {total}
-------------------------------------------------------------
''')

# Printing thank you message and centering it
print("Thank you for shopping with us!".center(70))
print("Please visit again!".center(70))


'''
Output:-

┌─[✗]─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $python pp/exp7/3.py

=============================================================
                       GROCERY BILL
=============================================================

-------------------------------------------------------------
Item           Quantity     Price (Rupees)     Total (Rupees)
-------------------------------------------------------------

apple              5             150.0            750.0     
banana             3             75.0             225.0     
orange             2             110.0            220.0     
bread              2             195.0            390.0     
milk               1             130.0            130.0     
eggs               12            120.0            1440.0    
cheese             1             250.0            250.0     
chicken            2             300.0            600.0     
rice               3             135.0            405.0     
pasta              2             95.0             190.0     

-------------------------------------------------------------
Total:                                           ₹ 4600.0
-------------------------------------------------------------

                   Thank you for shopping with us!                    
                         Please visit again!                          
┌─[aditya@aditya-hplaptop15da0xxx]─[~/Code/sy]
└──╼ $
'''
