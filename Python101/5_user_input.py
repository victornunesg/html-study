# --------------------------------
# USER INPUT
# --------------------------------

print('--------------------------------')
print('User input')
print('--------------------------------')

user_name = input('What is your name? ')
user_age = input('What is your age? ')
print('Hello ' + user_name + '!')
print('You are ' + user_age + ' years old!')
print('')
num1 = input('Enter a number: ')
num2 = input('Enter a second number:')
answer = float(num1) + float(num2)
# we need to cast the numbers due to the type received when user inputs the digits be a string
# otherwise the result will be the two numbers concatenated
print('The addition result is: ' + str(answer))  # other cast to put the number answer as a string
print('')

print('Exercise')
user_name = input('What is your name? ')
distance_km = input('What is the distance (in km)? ')
distance_miles = float(distance_km) / 1.609
print('')
print(f'Hello {user_name.title()}! \nYour distance is {distance_km} km or {round(distance_miles,2)} miles')
print('')
