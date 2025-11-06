while True:
    temperature = float(input("Enter temperature:"))
    if temperature <0:
        print(f"Freezing- stay inside")
    elif temperature <10:
        print(f"Very cold - wear coat")
    elif temperature < 20:
        print(f"Cool - jacket needed")
    elif temperature < 30:
        print(f"Pleasant")
    else:
        print("Hot - stay hydrated")
    again = input(f"Enter another temperature (yes or no)")
    if again != "yes":
        print("Be safe")
        break 
