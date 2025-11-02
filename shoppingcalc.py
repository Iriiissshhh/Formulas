item = input("What item are you purchasing?")
price = int(input("How much is the item?"))
quantity = int(input("How many items do you need?"))
total_before_discount = price * quantity
discount = int(input("What is the discount percentage?"))
discount_price= total_before_discount * (discount/100)
total_after_discount = total_before_discount - discount_price
print("The final price of the item is",total_after_discount)