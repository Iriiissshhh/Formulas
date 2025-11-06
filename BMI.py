weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in metres"))
BMI = weight/  (height * height) 
if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    if BMI < 18.5:
       print("You are underweight")
    elif BMI < 25:
        print("You are normal")
    elif BMI < 30:
        print("You are overweight")
    else:
        print("You are obese")