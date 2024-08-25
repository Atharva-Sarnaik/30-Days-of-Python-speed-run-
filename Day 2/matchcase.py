# Matchcase Statement
# Once a case is matched, break statement automatically executes
a=int(input("Enter the value of a:"))
match a:
    case 0:
        print("a is 0")
    case 2:
        print("a is 2")
    case _ if(a>10):
        print("a is greater than 10")
    case _ if(a!=90):
        print("a is not 90")

# Output 
'''
Enter the value of a:90
a is greater than 10
'''
