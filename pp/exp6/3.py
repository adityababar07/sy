from datetime import date

# Storing the information about shares
details = (("tata", '02/04/24', 500, 1, 650), ("reliance", '03/04/24', 700, 2, 850), ("tata", '02/04/24', 500, 1, 550))

choice = input("Do you want to enter portfolio details (y/n):\t")

if choice == "y":
    detail = []
    print("All the fields should be entered otherwise portfolio details won't be entered!!!!!")
    share_name = input("Enter name of share:\t")
    response = input("Have you bought this share today (y/n):\t")
    if response == "y":
        date_of_purchase = date.today()
    else:
        date_of_purchase = input("Enter date of purchase (DD/MM/YY):\t")
    cost_of_share = int(input("Enter cost of share:\t"))
    no_of_share = int(input("Enter no. of shares purchased:\t"))
    selling_price = int(input("Enter selling price:\t"))
    detail.append(share_name)
    detail.append(date_of_purchase)
    detail.append(cost_of_share)
    detail.append(no_of_share)
    detail.append(selling_price)
    detail = tuple(detail)
    details = list(details) 
    details.append(detail)
    details= tuple(details)

# Calculating total cost and profit/loss percentage
# total cost = no. of shares of each stock*price of share

total_cost_of_portfolio = 0
total_amount_gained = 0

for detail in details:
    detail = list(detail)
    total_cost_of_portfolio += detail[2]*detail[3]
    total_amount_gained += detail[4]-detail[2]

percentage_of_profit = (total_amount_gained/len(details))/100

print(f"The total cost of portfolio is:\t {total_cost_of_portfolio}")

if total_amount_gained > 0:
    print(f"The total amount gained is:\t {total_amount_gained}\n The total amount lost is :\t {0}")
    print(f"Percentage of profit :\t {percentage_of_profit} %")
    print(f"Percentage of loss :\t {0} %")
else:
    print(f"The total amount gained is:\t {0}\n The total amount lost is :\t {abs(total_amount_gained)}")
    print(f"Percentage of profit :\t {0} %")
    print(f"Percentage of loss :\t {abs(percentage_of_profit)} %")

'''
Output:-

@adityababar07 ➜ /workspaces/sy-pp- (master) $ python3 pp/exp6/3.py
Do you want to enter portfolio details (y/n):   y
All the fields should be entered otherwise portfolio details won't be entered!!!!!
Enter name of share:    tata steel
Have you bought this share today (y/n): y
Enter cost of share:    790
Enter no. of shares purchased:  67
Enter selling price:    799
The total cost of portfolio is:  55330
The total amount gained is:      359
 The total amount lost is :      0
Percentage of profit :   0.8975 %
Percentage of loss :     0 %
@adityababar07 ➜ /workspaces/sy-pp- (master) $ 
'''