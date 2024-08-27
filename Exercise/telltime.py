import time
timestamp=(time.strftime("%H/%M/%S"))
print(timestamp)
times=int(time.strftime("%H"))
if(times>4 and times<12):
    print("Goodmorning sir its",times,"am now")
elif(times>=12 and times<17):
    print("Goodafternoon sir its",times,"pm now")
elif(times>16 and times<21):
    print("Goodevening sir its",times,"pm now")
else:
    print("Goodnight")

# Output
'''
22/52/35
Goodnight
'''
