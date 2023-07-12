# basic_backend.py

# importing this file to handle exceptions when trying to create duplicate items or read non-existent items
import mvc_exceptions as mvc_exc

# global variable where we keep the data
items = list()


# 2 problems can impact this construction
# the first one is: duplicated items can be created without any restriction
# the second one is: if you try to read an item not previously specified, your application will crash
# therefore an exception file was created to handle those 2 cases above 'mvc_exceptions'
# the exception clauses were handled inside the functions using if conditional

# creation functionality
def create_item(name, price, quantity):
    global items
    exception = list(filter(lambda x: x['name'] == name, items))  # checking if the item already belongs to stock
    if exception:
        raise mvc_exc.ItemAlreadyStored(f'Item {name} is already stored')  # if duplicated, raise the exception
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})  # else, appends the list


def create_items(app_items):
    global items
    items = app_items


# reading functionality
def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(f'The item {name} is not stored, impossible to read.')


def read_items():
    global items
    return [item for item in items]


def update_item(name, price, quantity):
    global items
    position = list(filter(lambda x: x[1]['name'] == name, enumerate(items)))  # checking in what position element is
    print(position)
    if position:
        i, item_to_update = position[0][0], position[0][1]
        print(i)
        print(item_to_update)
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(f'Can\'t update "{name}" because it\'s not stored')


def delete_item(name):
    global items
    position = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if position:
        i, item_to_delete = position[0][0], position[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(f'Can\'t delete "{name}" because it\'s not stored')


# main function to test all the functionalities
def main():
    # list of dictionaries to simulate grocery shop stock, like a SQL database
    my_items = [
        {'name': 'bread', 'price': 0.5, 'quantity': 20},
        {'name': 'milk', 'price': 1.0, 'quantity': 10},
        {'name': 'wine', 'price': 10.0, 'quantity': 5},
    ]

    # CREATE
    create_items(my_items)
    create_item('beer', price=3.0, quantity=15)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())


if __name__ == '__main__':
    main()
