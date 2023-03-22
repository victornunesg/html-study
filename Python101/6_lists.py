# ----------------------------
# LISTS
# ----------------------------
print('--------------------------------')
print('Lists')
print('--------------------------------')

# Very similar to variables
# Can storage multiple data and mix different types of data

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
#  index:    0         1         2       3         4
print(friends[2])  # printing 'Terry'
print(friends[-1])  # printing Graham
print(friends[2:4])  # will not print 'Graham'
print(friends[:])  # hole list
print(len(friends))  # checking how many elements this list has
print(friends.index('Eric'))  # checking in what position one element is
print(friends.count('Eric'))  # checking how many occurrences one element has in the list

# sorting a list
print('')
print(friends)
friends.sort()  # sorts in crescent order
print(friends)
friends.sort(reverse=True)  # sorts in decreasing order
print(friends)
friends.reverse()  # reverses the order of the original string
print(friends)

cars = [911, 130, 328, 535, 740, 308]
print('')
print(min(cars))  # lowest number in the list
print(max(cars))  # highest number in the list
print(sum(cars))  # sum work with numbers only
print(min(friends))  # alphabetic order
print(max(friends))  # alphabetic order

# add elements in a list
print('')
friends.append('TerryG')  # adding an element
print(friends)
friends.insert(1, 'Victor')  # specifying in which position we want to add an element
print(friends)
friends[0] = 'William'  # changed the value of the 0 position
print(friends)

# extend lists, merge them
print('')
friends.extend(cars)
print(friends)
friends.remove('Terry')  # just remove a list item, needs to be specified
friends.pop(2)  # by default removes the last item in the list, different from remove,
# using pop you release memory in the program
friends.clear()  # empty list
del friends  # now the list is gone
del cars[2]  # removing index 2 from the list

# copying lists
print('')
new_cars = cars[:]
# new_cars = cars.copy()  # does the same thing as the line above
# new_cars = list(cars)  # does the same thing as the line above
print(cars)
print(new_cars)

# Exercise - lemonades
sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

# Getting the number of the last day of sell - 1st option
sales_w2.append(int(input('Inform the number of lemonades sold in the last day: ')))

# Getting the number of the last day of sell - 2nd option
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))

# Combining the 2 lists to put in sales list - 1st option
sales.extend(sales_w1)
sales.extend(sales_w2)

# Combining the 2 lists to put in sales list - 2nd option
sales = sales_w1 + sales_w2
sales.sort()

# Combining the 2 lists to put in sales list - 3rd option
sales = [x + y for x, y in zip(sales_w1, sales_w2)]

print(sales_w1)
print(sales_w2)
print(sales)
print('')

worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5

print(f'Best day: Separately = {max(max(sales_w1),max(sales_w2))} // General: {max(sales)}')
print(f'Worst day: Separately = {min(min(sales_w1),min(sales_w2))} // General: {min(sales)}')

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')
