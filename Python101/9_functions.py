# ----------------------------
# FUNCTIONS
# ----------------------------
# Always declare a function before using it
# After declaring, all the lines dented will be part of the function
def greeting():
    print('Hello friend!')


greeting()  # calling a function

# Using a function with a parameter


def greeting(name1):
    print(f'Hello {name1}!')


greeting('Brian')  # calling a function

# Using a function with multiple parameters


def greeting(name2, age2):
    print(f'Hello {name2}, you are {age2} years old!')


greeting('Brian', '29')  # calling a function

# Using a function with default parameter value


def greeting(name3, age3='28'):
    print(f'Hello {name3}, you are {age3} years old!')


greeting('Judith')  # calling a function

# Using a function with variable obtained by an input from user


def greeting(name4, age4):
    print(f'Hello {name4}, you are {age4} years old!')


name = input('Enter your name: ')
age = input('Enter your age: ')
greeting(name, age)  # calling a function

# ----------------------------
# EXERCISE
# ----------------------------
print('')
print('EXERCISE')
print('')
'''
def greeting(name, age=28):
    #Greets user with 'name' from 'input box' and 'age', if available, default age is used
    print('Hello '  +  name + ', you are ' + str(age) +'!')
    print(f'Hello {name}, you are {age} years old!')

name = input('Enter your name: ')
age = input('Enter your age: ')
greeting(name, age)
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase
'''


def greeting(name5, age5=28, color1='red'):
    # Greets user with 'name' from 'input box', 'color' 'age'. If unavailable, default age and color are used
    print('')
    print(f'Hello {name5.capitalize()}, you will be {age5+1} years old next birthday!')
    print(f'We hear you like the color {color1.lower()}!')


name5 = input('Enter your name: ')
age5 = input('Enter your age: ')
color1 = input('Enter a color you like: ')
print('')
greeting(name5, int(age5), color1)

# Named notation: it's best to name the arguments when calling the function to let the program more readable
# and also to be possible to change the order of the arguments
print('')
greeting(age5=29, color1='gray', name5='Victor Gomes')

# ----------------------------
# RETURN STATEMENTS
# ----------------------------

# Sometimes we want a function to give us a data back, in return


def value_added_tax(amount):
    tax = amount * 0.25


print('')
print(value_added_tax(100))  # in this case it will return 'none'

# Modifying the function to return a data


def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return amount, tax, total_amount  # when we have more than 1 item returned, Phyton return us a tuple
# return [amount, tax, total_amount]  # now a list will be outputted
# return {amount, tax, total_amount}  # now a set will be outputted
# return f'{amount}, {tax}, {total_amount}'  # now a string will be returned


print('')
price = value_added_tax(100)
print(price)  # a list will be returned
# print(price[1])  in this case only the tax will be returned
