# ----------------------------
# CONDITIONALS
# ----------------------------
print('')
print("Conditionals: IF statements")
print('')

is_raining = False
is_cold = True
print('Good morning!')
if is_raining or is_cold:  # one of the options is true
    print('Bring umbrella or jacket or both')
else:
    print('Umbrella is optional')

print('')
if is_raining and is_cold:  # both options needs to be true
    print('Bring umbrella and jacket')
else:
    print('Umbrella is optional')

print('')
is_raining = False
is_cold = False
print("Good Morning")
if is_raining and is_cold:  # raining and cold
    print("Bring Umbrella and jacket")
elif is_raining and not is_cold:  # raining and not cold
    print("Bring Umbrella")
elif not is_raining and is_cold:  # not raining and cold
    print("Bring Jacket")
else:  # not raining and not cold
    print("Shirt is fine!")

print('')
amount = 51
if amount <= 50:
    print('Purchase approved')
else:
    print('Please enter your pin!')

# The difference between using an if and an elif is?
# If's: each one of the ifs get checked
# Elif's: it will only check until it finds something that is correct, and stop after that

# ----------------------------
# EXERCISE
# ----------------------------
print('')
print('EXERCISE #1')
print('')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

operation = str(input('Please enter the operation (+, -, * , / or cf): '))
if operation not in ('+', '-', '/', '*', 'cf'):
    print('Input error, please input a valid one next time.')
else:
    num1 = float(input('Please enter the 1st number: '))
    if operation.upper() == 'CF':
        answer = num1 * 9 / 5 + 32
        print(f'{num1} Celsius is {answer} Fahrenheit')
    else:
        num2 = float(input('Please enter the 2nd number: '))
        if operation == '+':
            answer = num1 + num2
            print(f'The answer of {num1} + {num2} is: {answer}')
        elif operation == '-':
            answer = num1 - num2
            print(f'The answer of {num1} - {num2} is: {answer}')
        elif operation == '*':
            answer = num1 * num2
            print(f'The answer of {num1} * {num2} is: {answer}')
        elif operation == '/':
            answer = num1 / num2
            print(f'The answer of {num1} / {num2} is: {answer}')


# ----------------------------
# EXERCISE #2
# ----------------------------
print('')
print('EXERCISE #2')
print('')
# optimize/shorten the code in the function (optimized already)
# try to reduce the number of conditionals


def num_days(month):
    days = 31
    if month in {'apr', 'jun', 'sep', 'nov'}:
        days = 30
    elif month == 'feb':
        days = 28
    print(f'number of days in {month} is {days}')


num_days('feb')
