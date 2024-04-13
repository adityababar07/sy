from datetime import date
# storing the information about shares

details = (("tata", '02/04/24', 500, 1, 650), ("reliance", '03/04/24', 700, 2, 850), ("tata", '02/04/24',   500, 1, 550))

choice = input("Do you want to enter portfolio details (y/n):\t")

if choice == "y":
    detail = []
    print("All the fields should be entered otherwise portfolio details won't be entered!!!!!")
    share_name = input("enter name of share:\t")
    response = input("have you bought this share today (y/n):\t")
    if response == "y":
        date_of_purchase = date.today()
    else:
        date_of_purchase = input("enter date of purchase:\t")
    cost_of_share = int(input("enter cost of share:\t"))
    no_of_share = int(input("enter no. of shares purchased:\t"))
    selling_price = int(input("enter selling price:\t"))
    detail.append(share_name)
    detail.append(date_of_purchase)
    detail.append(cost_of_share)
    detail.append(no_of_share)
    detail.append(selling_price)
    detail = tuple(detail)
    details = list(details) 
    details.append(detail)
    details= tuple(details)

# changes from here 

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
