# ----------------------------
# FOR LOOPS
# ----------------------------

print('')
print('For loops')
print('')
# In for loops we already now how many interactions will be performed in advance
for letter in 'Norwegian blue':  # 'letter' is the variable
    # the variable letter is used in 'for' loop to pick each one of characters in the string to write one by one
    print(letter)  # now the letters are getting printed one by one

print('')
print("For Loop done!")
print('')

for number in range(8):
    # the variable number is used in 'for' loop to pick each one of the numbers from 0 to 7 to write one by one
    print(number)

print('')
print("For Loop done!")
print('')

for step in range(1, 15, 3):
    # the variable number is used in 'for' loop to pick each one of the numbers from 1 to 15 in steps of 3
    print(step)

print('')
print("For Loop done!")
print('')

for name in ['John', 'Terry', 'Eric', 'Michael', 'George']:
    # the variable number is used in 'for' loop to pick each one of the names in the list above
    print(name)

print('')
print("For Loop done!")
print('')

names = ['John', 'Terry', 'Eric', 'Michael', 'George']
for name in names:
    # the variable number is used in 'for' loop to pick each one of the names in the list names above
    print(name)

print('')
print("For Loop done!")
print('')

# Break and Continue statements
friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        break  # in this case it will find John, Terry and Eric and will jump out of the loop afterwards
    print(friend)

print('')
print("For Loop done!")
print('')

friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        continue  # in this case it will find John, Terry and Eric and will continue the others
        # continues inside the for loop
    print(friend)

print('')
print("For Loop done!")
print('')

# Nested loops - a loop inside another loop

friends = ['John', 'Terry', 'Eric']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)

print('')
print("For Loop done!")
print('')


# ----------------------------
# EXERCISE
# ----------------------------

print('')
print('EXERCISE')
print('')
names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
invitation_list = []
invitation_list.extend(names)
invitation_list.extend(names1)
print(invitation_list)
print('')

invitation_list.append(input('Enter the 1st extra name: '))
invitation_list.append(input('Enter the 2nd extra name: '))
invitation_list = (','.join(invitation_list)).title().split(',')
print(invitation_list, type(invitation_list))
print('')

for invite in invitation_list:
    print(f'{invite}! You are invited to the party on Saturday!')
