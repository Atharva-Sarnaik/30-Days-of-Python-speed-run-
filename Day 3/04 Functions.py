# Functionn Definition

def tofind(a,b):
    if(a in b):
        print("a exists in b")
    else:
        print("a is not in b or is different")

a=["1","2"]
b=[["1","2"],"3","4"]
tofind(a,b) # Function Calling

# Names of parameters can be different as well, for eg

def isgreater(c,d):
    if(c>d):
        print("First number is greater")
    else:
        print("second number is greater or equal")
    
i=100
j=98
isgreater(i,j)

# Output
'''
a exists in b
First number is greater
'''
