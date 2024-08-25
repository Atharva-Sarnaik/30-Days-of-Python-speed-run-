# Using "time" module to get the time as output
# Using "strftime" function which gives hours, minutes and seconds

import time
timestamp=time.strftime("%H/%M/%S")
print(timestamp)
timestamp=time.strftime("%H")
print(timestamp)
timestamp=time.strftime("%M")
print(timestamp)
timestamp=time.strftime("%S")
print(timestamp)

# Using if else to get Output according to the time.

import time
timestamp=(time.strftime("%H/%M/%S"))
print(timestamp)
timestamp=int(time.strftime("%H"))
if(timestamp<12):
    print("Good Moring sir its",timestamp,"am now")
elif(timestamp>12):
    print("Good Afternoon sir its",timestamp,"pm now")

# Output
'''
15/43/08
15
43
08
15/55/27
Good Afternoon sir its 15 pm now
'''
