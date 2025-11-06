score = int(input("What is your score?"))
if score <0 or score >100:
    print("Invalid input")
else:
    if score >=90:
        print("You have an A")
    elif score >=80:
        print("You have a B")
    elif score >=70:
        print("You have a C")
    elif score >=60:
        print("You have a D")
    else:
        print("You have an F")