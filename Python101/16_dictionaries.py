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

# ----------------------------
# EXERCISE
# ----------------------------
# It’s...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to
# save your village, and probably some good-looking girl or boy you want to marry. All prices in gold pieces excl. VAT
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store
# inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken, in this version you don't have to pay for stuff or add it up

# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit',
# and to exit if a nonexistent item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about
# total cost and how much gold you have left

# ver 1.4 random bug fix, ' browser compatibility', refactoring code... basically being lazy ..stop scrolling TikTok

# Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all
# stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management..
# as in all games there is a special way to do this that actually makes money and solves the problem...
# can you find 'them'? Do you know why? May require knowledge of actual python 'lore'


# create stores
freelancers = {
    'name': 'freelancing Shop', 'brian': 70, 'black knight': 20,
    'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}

antiques = {'name': 'Antique Shop', 'french castle': 400,
            'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}

pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

# creating an empty dict to represent the cart
cart = {}

# creating a purse to represent a credit to be used in the shopping
purse = 1000

# this string will be used to inform the name and value of an item that has been bought
bought_items = ''

# creating a dict containing all the stores inventory to inform how it is before the selling
department_store = {}
for department in (freelancers, antiques, pet_shop):
    department_store.update(department)
department_store.pop('name')
print('Morning inventory of stores:')
print(sorted(department_store.items()))
print('-----------------')

# shopping begins, now we run through the shops, one by one
for shop in (freelancers, antiques, pet_shop):
    print('')
    print(f'Welcome to {shop["name"]}! These are the available items: ')
    print(f'{shop.keys()}'.lower())  # printing all shop items, in lowercase
    print('')
    buy_item = input('Enter the item to be bought or "exit" to go to the next shop: ')

    # if user type other thing will be moved to the next loop/shop
    if buy_item not in shop or buy_item == 'exit':
        continue  # moves to the next loop/interaction

    # updating the items bought adding the name and the value
    bought_items = bought_items + f'{buy_item}: {shop[buy_item]} Gp '

    # updating the dict cart, adding the bought item via pop statement
    # which means that the item will be popped from the store
    cart.update({buy_item: shop.pop(buy_item)})

    # bought_items = ", ".join(list(cart.keys()))  # creating a new variable to represent all the items bought
    # in this case we are turning the dictionary into a list first, then joining the list to get a string for better
    # representation to the user

# is important to mention that using pop will remove all the item from the shop, including its value
# by this way we don`t have a value reduction, it removes key and value from the original dict

print(cart)
total_cost = sum(cart.values())  # calculating the total amount
balance = purse - total_cost  # calculating the remaining balance
print('')
print(f'Congratulations, you`ve just bought: {bought_items}')  # here we are just printing the string of items bought
print(f'Total cost: {total_cost} Gp / Balance: {balance} Gp')  # informing user the shopping details

# creating a dict containing all the stores inventory to inform how it is after the selling
department_store_after = {**freelancers, **antiques, **pet_shop}  # pyth 3.5
department_store_after.pop('name')
print('-----------------')
print('Evening inventory of stores', sorted(department_store_after.items()))
