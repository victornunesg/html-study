# ----------------------------
# ENUMERATE
# ----------------------------

print('python101 - Enumerate')
friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

# Numbering a list, without using an iterator:

for num, friend in enumerate(friends, 1):  # the second attribute is used to define the starting number
    print(num, friend)

print('')

for num, friend in enumerate(friends, 51):  # the second attribute is used to define the starting number
    print(num, friend)

print('')

for num, friend in enumerate(friends, 1):  # the second attribute is used to define the starting number
    print(num, friend)

# What the enumerate function actually does:
efriends = [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta'), (4, 'Colin')]
# Turns the elements inside the list into tuples, putting the number in front of them

print('')
print(type(enumerate(friends)))  # turns into a separated class, called enumerate
print(list(enumerate(friends)))  # we get the tuples inside the list, as described at line 24

print('')
for num, letter in enumerate('python', start=5):  # using enumerate with a string
    print(num, letter)


