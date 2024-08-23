name="Atharva"
length=len(name) # Gives the length of string
print(length) 
# Slicing can be donen using square brackets"[]"
# Index starts from 0 
# While slicing, last index will not get printed, here 1 will not get printed
print(name[0:1])
print(name[1:2])
print(name[2:6])
# print(name[len(name)-5:len(name)-1]), THIS WILL BE DONE IF NEGATIVE NUMBERS ARE USED IN SLICING
print(name[-5:-1])
print(name[-3:-2])

#Output
'''
7
A
t
harv
harv
r
'''
