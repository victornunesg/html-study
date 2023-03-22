# ----------------------------
# COMPREHENSIONS - LISTS
# ----------------------------
print('\n Comprehensions - Lists')
print('----------------------')
# Allows to created lists, sets, dictionaries with less code
# Anything you can do with comprehensions you can also do with for loops
# The comprehension contains the same code as for loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# give me a list with num squared for each num in numbers
new_list = []
for num in numbers:
    new_list.append(num*num)  # getting number by number and creating a new one with the square numbers
print('\n', new_list)

# doing the same thing as for loop above using comprehensions, with less code:
new_list = [num*num for num in numbers]
print('\n', new_list)

# give me a list with num for each num in numbers if num is even
new_list = [num for num in numbers if num % 2 == 0]
print('\n', new_list)

# using filter and lambda function to do it: (more complicated)
new_list = filter(lambda num1: num1 % 2 == 0, numbers)
print('\n', list(new_list))  # filter will bring an object filtered, so we must turn into a list

# Other exemple: I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
new_list = []
for letter in 'spam':
    for num in range(4):
        new_list.append((letter, num))
print('\n', new_list)

# doing the same thing as for loop above using comprehensions, with less code:
new_list = [(letter, num) for letter in 'spam' for num in range(4)]
print('\n', new_list)

# ----------------------------
# COMPREHENSIONS - DICTIONARIES
# ----------------------------
print('\n Comprehensions - Dictionaries')
print('----------------------')

# Dictionary comprehensions
movies = ["And Now for Something Completely Different", "Monty Python and the Holy Grail",
          "Monty Python's Life of Brian", "Monty Python Live at the Hollywood Bowl",
          "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)"]
year = [1971, 1975, 1979, 1982, 1983, 2014]
names = ['John', 'Eric', 'Michael', 'Graham', 'Terry', 'TerryG']

# create a list containing movies and year
print('\n', list(zip(movies, year)))  # combined as tuples inside a list

# give me a dict('movies': year) for each movie, year in zip(movies, year)
# using for loop - option #1
movies2 = {}
for movie in (list(zip(movies, year))):
    movies2.update(list(zip(movies, year)))
print('\n', movies2)

# using for loop - option #2
movies2 = dict()
for movie, yr in zip(movies, year):
    movies2[movie] = yr
print('\n', movies2)

# now using comprehensions to do the same stuff
movies2 = {movie: yr for movie, yr in zip(movies, year)}
print('\n', movies2)

# getting the movies before 1983 starting with 'Monty' (adding if clause)
movies2 = {movie: yr for movie, yr in zip(movies, year) if yr < 1983 and movie.startswith('Monty')}
print('\n', movies2)

# now we want to create a dict with name + movie + year:
n1 = [[name + "s favorite movie was '" + movie + "' from " + str(yr)] for name, movie, yr in zip(names, movies, year)
      if yr < 1981]
print('\n', n1)
