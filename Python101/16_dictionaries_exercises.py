"""
It’s...not really an adventure game...#Ver 1.0
Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to
save your village, and probably some good-looking girl or boy you want to marry. All prices in gold pieces excl. VAT
The code should allow you to get 1 thing from each store and each item you get should be removed from the store
inventory, then do same for next store...
one way to buy by typing the key 'newt' in an input box...or something
at end you should print the 'items' you have taken, in this version you don't have to pay for stuff or add it up

ver 1.2 add ability to exit a store without buying and go to next by typing 'exit',
and to exit if a nonexistent item is bought(typed)
Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about
total cost and how much gold you have left

ver 1.4 random bug fix, ' browser compatibility', refactoring code... basically being lazy ..stop scrolling TikTok

Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all
stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management..
as in all games there is a special way to do this that actually makes money and solves the problem...
can you find 'them'? Do you know why? May require knowledge of actual python 'lore'
"""


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