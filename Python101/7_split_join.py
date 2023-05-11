print('Welcome to Python 101: Split and Join')
# ----------------------------
print('\nSPLIT')
# ----------------------------
msg = 'Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

# Split transforms a string into a list
print(list(msg))  # Creates a list but splitting each character separately
print(msg.split())  # Now the string is transformed into a list with the words splitted separately
print(msg.split(':'))  # It is possible to define in the argument where you want to split the string

print('')

# ----------------------------
print('\nJOIN')
# ----------------------------
# Join does the opposite, transforms a list into a string
print(str(friends_list))  # Casting into a string does not bring the expected result, because it still looks like a list
print(','.join(friends_list))  # Now we have a string based on the list,
print('\n'.join(friends_list))  # Printing each item in a new line
# the first argument is the character you want to define as the separating character

print('')

# We can do multiple operations using split and join
# We also can use replace as an option, for example, to remove blank spaces in msg string:
print(''.join(msg.split()))
print(msg.replace(' ', ''))
print(' ')

# ----------------------------
print('\nEXERCISE')
# ----------------------------
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

print('EXERCISE')
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

print(csv)
print(csv.split(';'))
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
print(','.join(','.join(csv.split(';')).split(':')))
print((','.join(','.join(csv.split(';')).split(':'))).split(','))
print(' ')
friends_list = ((csv.replace(':', ',').replace(';', ',')).split(','))
print(friends_list)
