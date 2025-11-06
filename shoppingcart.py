item = (input("What item are you purchasing?"))
price = float(input("How much is it?(in dollars)"))
quantity = float(input("How many do you need?"))
price_before_discount = price * quantity
if price_before_discount > 50:
    discount = (10/100) * price_before_discount
    final_price = price_before_discount - discount
    print ("Your final price is",final_price)
else:
    print("Your final price is", price_before_discount)

