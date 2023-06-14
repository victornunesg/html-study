# ----------------------------
# SORT / SORTED
# ----------------------------
print('')
print('sort() and sorted()')
print('Immutability and return values')
print('')


my_list = [1, 5, 3, 7, 2]  # lists are mutable, we can change them
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}  # dictionaries are also mutable
my_tuple = ('d', 'c', 'e', 'a', 'b')  # tuples and strings are immutable, can`t be changed
my_string = 'python'  # there isn`t sort for them, because you can't change

# sort method does not return anything, it goes in and sorts the list

# the function sorted actually returns a new object, that has been sorted

print(my_list, 'original')
print(my_list.sort())  # we get nothing, because nothing is being delivered
print(my_list, 'new')  # now we get the sorted list printed

print('\nSorting Lists')
print(my_list, 'original   ')
print(sorted(my_list))  # with the function sorted, we receive a sorted list, because it returns the list
print(my_list, 'new - like original')  # but here, as the function does not record, we get the original list
my_list1 = sorted(my_list)  # here we name the new object that sorted() function generates
print(my_list1)  # the result is a new list, equivalent to the one sorted at line 24
print(list(reversed(my_list)))  # flips the list around, is necessary to cast into a list before using reverse
print(my_list[::-1])  # does the same thing above
print('')

print('Sorting Tuples')
# When we sort a tuple we don't actually get a tuple, it gives us a new list sorted
print(my_tuple, 'original')
print(sorted(my_tuple))  # a sorted list is created based on the tuple
print(my_tuple, 'new')
print('')

print('Sorting Strings')
# When we sort a tuple we don't actually get a tuple, it gives us a new list sorted
print(my_string, 'original')
print(sorted(my_string))  # a sorted list is created based on the string
print(my_string, 'new')
print('')

print('Sorting Dictionaries')
# When we sort a tuple we don't actually get a tuple, it gives us a new list sorted
print(my_dict, 'original')
print(sorted(my_dict))  # a sorted list is created based on the key values of the dictionary
print(sorted(my_dict.items()))  # we get the result as tuples inside a list, sorted at the key
print(sorted(my_dict.values()))  # a sorted list is created based on the values of the dictionary
print(sorted(my_dict.values(), reverse=True))  # sorted list is created based on the values of the dictionary in reverse
print(my_dict, 'new')
print('')

print('Another examples')
my_list = [1, 5, -3, 7, -2]
my_llist = [['car', 4, 65], ['dog', 2, 30], ['add', 3, 10], ['bee', 1, 24]]
print(sorted(my_list))  # considers the - signal
print(sorted(my_list, key=abs))  # absolute value, using 'key' feature and 'abs' function
# any function can be use after the 'key' feature
print(sorted(my_llist))  # list of lists has been sorted by first element

# lambda functions are throw away functions that you can write in one line
# in the case above we sorted by second element in the list, index=1
print(sorted(my_llist, key=lambda item: item[1]))  # item in the list we are trying to sort
