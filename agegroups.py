age = int(input("How old are you?"))
if age < 0 or age > 120:
    print("Invalid input")
else:
    if age <12:
       print("You are a child")
    elif age <19:
       print("You are a teen")
    elif age <64:
      print("You are an adult")
    else:
      print("You are a senior")
