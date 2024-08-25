# Nested if statements

num=int(input("Enter the number:"))
if(num>0):
    print('number is postive')
    if(num>0 and num<10):
        print("Number is between 1-10")
    elif(num>10 and num<20):
        print("Number is between 10-20")
elif(num==0):
    print('Number is zero')
else:
    print('Number is negative')

# Output
'''
Enter the number:-8
Number is negative
'''
