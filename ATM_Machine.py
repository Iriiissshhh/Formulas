balance = 1000
while True:
    menu = input("Select option (check balance, withdraw money, deposit money)").lower().strip()
    if menu == "check balance":
        print("Your balance is",balance)
    elif menu == "withdraw money":
        withdraw_money = int(input("Enter amount to withdraw:"))
        if withdraw_money > balance:
            print("Insufficient amount")
        else:
            balance = balance - withdraw_money
            print("Account balance is", balance)
    elif menu == "deposit money":
        deposit_money = int(input("Enter amount:"))
        balance = deposit_money + balance
        print("Your balance is",balance)
    else:
        print("exit")
    again = input("Do you want to continue?(yes or no)")
    if again != "yes":
        print("Process complete")
        break
