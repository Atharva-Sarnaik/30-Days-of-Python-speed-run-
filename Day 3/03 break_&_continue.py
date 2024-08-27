# Break statement
# Used to break out of the loop

for i in range(12):
    print("5 X ",i+1," = ",5*(i+1))
    i=i+1
    if(i==10):
        break

# Continue statement
# Used to skip the iteration and continue the loop until the loops condition is false

for i in range(12):
    if(i==10):
        print("Skip the iteration")
        continue
    print("5 X ",i+1," = ",5*(i+1))

# Output
'''
5 X  1  =  5
5 X  2  =  10
5 X  3  =  15
5 X  4  =  20
5 X  5  =  25
5 X  6  =  30
5 X  7  =  35
5 X  8  =  40
5 X  9  =  45
5 X  10  =  50
5 X  1  =  5
5 X  2  =  10
5 X  3  =  15
5 X  4  =  20
5 X  5  =  25
5 X  6  =  30
5 X  7  =  35
5 X  8  =  40
5 X  9  =  45
5 X  10  =  50
Skip the iteration
5 X  12  =  60
'''
