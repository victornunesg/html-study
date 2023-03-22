# --------------------------------
# STRINGS-BASICS/SLICING
# --------------------------------

print('--------------------------------')
print('Strings-Basics / Slicing')
print('--------------------------------')

msg = 'Strings examples in Python, it\'s interesting'
print(msg + msg)  # The messages will be printed without spaces in between
print(msg, msg)  # A space is given in between
print(msg*2)  # Same result as +
print(msg.upper())  # Uppercase all the string
print(msg.lower())  # Lowercase all the string
print(msg.capitalize())  # Only capitalize the first letter of the string
print(msg.title())  # Capitalize the first letter of each word in the string
print(len(msg))  # Prints the msg length
print(msg.count('python'))  # Case sensitive

print('')

# Slicing
print(msg[5])  # Getting the character in the 5th position of the string
print(msg[-1])  # Getting the last character in the string
print(msg[2:7])  # Getting characters from 2 to 7th positions
print(msg[:10])  # # Getting characters from 0 to 10th positions

print('')

msg = 'welcome to Python 101: Strings'
msg1 = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1].title())  # printing msg in backwards
print('')

# --------------------------------
# STRINGS-FIND/REPLACE, STRING FORMATTING
# --------------------------------

print('--------------------------------')
print('Strings-Find/replace, string formatting')
print('--------------------------------')
print('')

# Multi lines strings, using triple quotes
msg = """Dear Terry,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""

print(msg)
print(msg.find('D'))  # returns the position of `D` character starts
print(msg.find('Terry'))  # returns the position of `Terry` word starts
print(msg.replace('Terry', 'Victor'))  # changes words or characters, but it does not save the string after
print(msg)
msg = msg.replace('Terry', 'Victor')  # it is also possible to save the new message in the same variable msg as before
print(msg)

print('')

# Membership
print('Victor' in msg)  # Checking if 'Victor' exists in msg1, returns boolean
print('Victor' not in msg)  # Checking if 'Victor' does not exist in msg1, returns boolean

# String formatting
print('')
name = 'TERRY'
color = 'RED'
msg = '[' + name.capitalize() + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# msg1 gives the same result as msg, using formatting settings giving more clarity in the code
print(msg)
print(msg1)
print('')
