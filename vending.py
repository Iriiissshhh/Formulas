drink = input("What drink do you want? (coffee,tea or soda)").strip().lower()
sugar = input("Do you want sugar?(yes or no) ")
if drink == "coffee":
    milk = input("Do you want milk?(yes or no)").strip().lower()
    if milk == "yes" and sugar == "yes":
        print("You will have coffee with milk and sugar")
    elif milk == "yes" and sugar == "no":
        print("You will have coffee with milk and no sugar")
    elif milk == "no" and sugar == "yes":
        print("You will have coffee with sugar and no milk")
    else:
        print("You will have black coffee with no milk and no sugar")
elif drink == "tea":
    if sugar == "yes":
        print("You will have tea with sugar")
    else:
        print("You will have tea with no sugar")
else:
    print("You will have soda")
