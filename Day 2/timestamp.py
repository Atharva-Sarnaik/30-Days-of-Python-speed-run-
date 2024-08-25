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

# Output
'''
15/43/08
15
43
08
'''
