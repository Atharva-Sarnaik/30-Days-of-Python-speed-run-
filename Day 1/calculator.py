a=float(input("Enter the 1st number:"))
b=float(input("Enter the 2nd number:"))
c=int(input("Enter 1 to add\nEnter 2 to substract\nEnter 3 to Multiply\nEnter 4 to Divide\nEnter 5 to get the remainder\n"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    if b!=0:
        print(a/b)
    else:
        print("Error: Cannot divide by 0")
elif c==5:
    if b!=0:
        print(a%b)
    else:
        print("Error: Cannot divide by 0")
else:
    print("Invalid input")
