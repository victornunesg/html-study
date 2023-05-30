# ----------------------------
# DICTIONARIES
# ----------------------------
print('')
print('DICTIONARIES')
print('')


# Dictionaries stores name/value pairs or key/value pairs
# You look for a word/key, so you get a definition/value
# It is like a translation table key -> value
# Jan : January
# Feb : February
# É possível obter uma informação através de uma chave ao invés de index (não recomendado pegar pelo index).
# Não deve ser usado para pegar itens em uma determinada ordem
# Podem ter valores heterogêneos (vários tipos de valores em um mesmo dicionário)
# As chaves são únicas, obrigatoriamente. Caso haja a mesma chave para dois valores diferentes, um será ignorado.
# Let's define a movie dictionary:

movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
}
# We can actually use any kind of data types
print(movie)
print(movie['title'])  # printing just one item, title
print(movie.get('title'))  # does the same as above
# if you try to get something that does not exist in the dictionary, an error message will be given
# to avoid, we can use the 'get' method
print(movie.get('budget'))  # the results will be an empty object, 'none'
print(movie.get('budget', 'not found'))  # we also can set a default value for non-existent items
print(movie)
print('')

# Updating an item and also defining new ones
movie['title'] = 'The Holy Grail'  # updating an entry individually
# updating all the dictionary with update command:
movie.update({'title': 'The Holy Grail', 'year': 1975, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']})
movie['budget'] = 2500  # setting new entry to the dictionary
print(movie)
print('')

# Deleting entries
del movie['year']  # deleting individually
movie.pop('budget')  # using pop, same as lists, releases memory allocation of your code
print(movie)
print('')
print(len(movie))  # checking how many entries we have in the dictionary
print(movie.keys())  # printing the dictionary keys
print(movie.values())  # printing the dictionary values
print(movie.items())  # brings the dictionary in tuples

# Looping into entries in a dictionary
print('')
for key in movie:  # only one item
    print(key)

for key, value in movie.items():
    print(key, value)

# Membership tests
# Dictionaries aren't ordered, can't contain duplicated values (at least the keys)
print('')
python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}

print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here')

# Putting dictionaries together
people = {}
people1 = {}
people2 = {}

# method 1 = update
people.update(python)  # copying python dictionary into people
print(people)
people.update(holy_grail)  # already have python dictionary, adding holy grail
print(people)
people.update(life_of_brian)  # already have python dictionary, adding holy grail
print(people)
print('')

# method 2 = comprehension
for groups in (python, holy_grail, life_of_brian):
    people1.update(groups)
print(people1)
print('')

# method 3 = unpacking
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)
print('')

# sorting items
print(sorted(people.items()))
print(sorted(people1.items()))
print(sorted(people2.items()))
print('')

# calculating sum (only if values are numbers, otherwise an error will occur)
print('The sum of the ages: ', sum(people.values()))
print('')


