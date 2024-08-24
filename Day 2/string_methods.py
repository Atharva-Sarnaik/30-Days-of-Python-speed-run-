# Strings are Immutable

a="!!!!!wow!!!!!!"
print(len(a)) # Give length
print(a)
print(a.upper()) # Capitalizes all letters in string
print(a.lower()) # Lowercases all letters
print(a.rstrip("!")) # Strips/Removes the "!", but keeps the left ones as it is
print(a.replace("wow","omg")) # replaces the word with new entered one
b="buGatti CHiron"
print(b.capitalize()) # Capitalize 1st letter and lowercases all other even if they are capital
print(len(b))
print(b.center(50)) # Puts space behind the string
print(len(b.center(50)))
print(a.count("wow")) # Counts how many "wow" are there in the string
print(b.endswith("on")) # Evaluates if the string ends with these letters
print(b.startswith("bu")) # # Evaluates if the string starts with these letters
print(b.endswith("CHi",5,11)) # Evaluates if these letters exist between index 5 and 11, of the string
c="he is a very good person"
print(c.find("very")) # Gives the index of "very" # returns "-1" if entered character is not found
#print(c.index("veryyyy")) # Returns error if entered character is not found
bike="HondaCB350"
game="witcher 3\n"
print(bike.isalnum()) # Prints true if alpha numerics ("A-Z,a-z,0-9") are present.
print(bike.isalpha()) # Prints true if aiphas ("A-Z,a-z") are present
print(game.islower()) # Prints true if string contains all lowercase characters
print(bike.isupper()) # Prints true if string contains all uppercase characters
print(game.isprintable()) # Prints true if all characters inside the string are printable
d="      "   "       "
print(d.isspace()) # Prints true if wide spaces are found
print(game.istitle()) # Prints true if first letter of each word is capital
print(game.swapcase()) # Prints all in uppercase if it is lowercase and vice versa
print(game.title()) # Makes the first letter of each word uppercase

# Output
'''
14
!!!!!wow!!!!!!
!!!!!WOW!!!!!!
!!!!!wow!!!!!!
!!!!!wow
!!!!!omg!!!!!!
Bugatti chiron
14
                  buGatti CHiron
50
1
True
True
True
8
True
False
True
False
False
True
False
WITCHER 3

Witcher 3
'''
