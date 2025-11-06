drink = input("What drink will you have?(tea,soda,water,coffee,beer)")
sugar = input("Will you have sugar?(yes or no)").lower().strip()
if drink == "coffee":
    milk = input("Do you want it with milk?(yes or no)")
    if sugar == "yes" and milk == "yes":
        print("You will have coffee with sugar and milk")
    elif sugar == "no" and milk == "yes":
        print("You will have coffee with milk but no sugar")
    elif sugar == "yes" and milk == "no":
        print("You will have coffee with sugar but no milk")
    else:
        print("You will have black coffee with no sugar")
elif drink == "tea":
    if sugar == "yes":
      print("You will have tea with sugar")
    else:
        print("You will have tea with no sugar")
elif drink == "soda":
    if sugar == "yes":
        print("You will have soda with added sugar")
    else:
        print("You will have soda with no added sugar")
elif drink == "beer":
     type = input ("Which beer will you have?(Balozi, tusker, guiness, pilsner,tusker cider, black ice, savannah)")
     if sugar == "yes":
         print("You will have", type, "with added sugar")
     else:
         print("You will have",type,"with no added sugars")
else:
    print("You will have water")    