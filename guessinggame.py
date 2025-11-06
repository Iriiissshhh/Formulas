while True:
    number = 8
    guess = int(input("Enter guess:"))
    if guess > number:
        print("Number is too high")
    elif guess < number:
        print("Number is too small")
    else:
        print("Number is correct")
    again = input("Do you want to play again(yes or no)").lower().strip()
    if again != "yes":
        print("Game over")
        break 