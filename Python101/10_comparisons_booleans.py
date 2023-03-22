# ----------------------------
# COMPARISONS
# ----------------------------

print('')
print('Comparisons')
print('')

a = 7  # assignment operator, assign a value to a variable
b = 3

print('a = ', a)
print('b = ', b)
print('a == b is', a == b)  # checking if 'a' is equal to 'b'
print('a != b is', a != b)  # checking if 'a' is not equal to 'b'
print('a > b is', a > b)  # checking if 'a' is greater than 'b'
print('a < b is', a < b)  # checking if 'a' is less than 'b'
print('a >= b is', a >= b)  # checking if 'a' is greater than or equal to 'b'
print('a <= b is', a <= b)  # checking if 'a' is less than or equal to 'b'

# in operator, denotes membership
print('')
print('o in John is ', 'o' in 'John')  # checking if 'o' is found the string 'John'
print('o in John is ', 'o' not in 'John')  # checking if 'o' is not found the string 'John'
print('John is John is ', 'John' is 'John')  # identity
print('John is not John is ', 'John' is not 'John')  # negative identity

# identity operator, checks if two things are identical
print('')
a = [3, 7, 42]
b = [3, 7, 42]
print(a == b)  # returns True because 'a' looks like 'b', they are equal (in value)
print(a is b)  # returns False because 'a' does not occupy the same memory space of 'b', they are not identical
print(id(a), id(b))  # shows the memory position of each one

# ----------------------------
# BOOLEANS
# ----------------------------

print('')
print('Booleans')
print('')
print(int(True))  # making 'True' boolean into integer returns 1
print(int(False))  # making 'False' boolean into integer returns 0
print(bool('Parrot'))  # transforming a string into boolean returns 'True'
print(bool(' '))  # transforming a string with a space into boolean also returns 'True'
print(bool(1))  # transforming objects different from zero into boolean returns 'True':
print(bool(50.2))  # float
print(bool([1, 2]))  # lists

# Empty objects and zeros when turned into boolean return 'False'
print(bool(''))  # transforming an empty string into boolean returns 'False'
print(bool(0))  # transforming a zero into boolean returns 'False'
print(bool([]))  # transforming an empty list into boolean returns 'False'

# Trivial values evaluate to zero
# Not trivial values to one

# Boolean values can be converted to numbers:
print(42 + True)  # shows 42 + 1 = 43
print(42 + False)  # shows 42 + 0 = 42
