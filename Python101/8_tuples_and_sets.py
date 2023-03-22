# ----------------------------
# TUPLES
# ----------------------------
# Tuples - faster Lists you can't change
# They are faster to work with than regular lists
# The only code difference is: use () instead of []

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
print(friends)
print(friends_tuple)

# We can access the elements in the same way, also slice
# But we can't use append, insert because tuples are immutable, just the functions to get data from it
print(friends[2:4])
print(friends_tuple[2:4])

# ----------------------------
# SETS
# ----------------------------
# Sets - blazingly fast unordered Lists
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric', 'Eric'}

print(friends)
print(friends_tuple)
print(friends_set)

# Main difference, set is unordered and removes duplicated values
# It is way faster to search in it than regular lists

my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
print(friends_set.intersection(my_friends_set))  # gives the indexes in common between two sets
print(friends_set.difference(my_friends_set))  # gives the indexes different between two sets
print(friends_set.union(my_friends_set))  # all names in both sets with no duplicates

# ----------------------------
# EMPTY TYPES OF LIST CREATION
# ----------------------------
# Creating empty types of lists:
# empty Lists
empty_list = []
empty_list = list()

# empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# empty Set
empty_set = {}  # this is wrong, this is a dictionary
empty_set = set()

# ----------------------------
# EXERCISE
# ----------------------------
print('')
print('EXERCISE')
print('')
# 1. Check if ‘Eric’ and ‘John’ exist in friends
# 2. combine or add the two sets
# 3. Find names that are in both sets
# 4. find names that are only in friends
# 5. Show only the names who only appear in one of the lists
# 6. Create a new cars-list without duplicates

friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']
john = {'John', 'Eric'}

# 1. Check if ‘Eric’ and ‘John’ exist in friends
print(friends.intersection(john))
print('Eric' in friends and 'John' in friends)

# 2. combine or add the two sets
print('')
print(friends.union(my_friends))
print(friends | my_friends)  # other way to union sets

# 3. Find names that are in both sets
print('')
print(friends.intersection(my_friends))
print(friends & my_friends)  # other way to get the intersection between sets

# 4. find names that are only in friends
print('')
print(friends.difference(my_friends))
print(friends - my_friends)  # other way to get the difference between sets

# 5. Show only the names who only appear in one of the lists
print('')
print(my_friends.symmetric_difference(friends))
print(my_friends ^ friends)  # other way to get only the results that does not repeat between sets

# 6. Create a new cars-list without duplicates
cars_new = set(cars)  # now we created a set of cars without duplicated values
cars_new = list(set(cars))  # and now we turned back into a list, without duplicated values
print(cars)
print(cars_new)
