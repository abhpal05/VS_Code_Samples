# Odd or Even
n1 = int(input("Enter number: "))
if((n1 % 2) == 0):
    print("The number is even.")
else:
    print("The number is odd.")

# If the number is multiple of 4
if(n1%2 == 0):
    if(n1%4 == 0):
        print("The number is a multiple of 4")
    else:
        print("The number is not a miltiple of 4")