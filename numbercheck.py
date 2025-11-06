number = int(input("Enter number:"))
if number > 0:
    if number %2==0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
elif number <0:
     if number %2 == 1:
         print("Number is negative and odd")
     else:
        print("Number is negative and even")
else:
    print("Number is zero")