# ----------------------------
# WHILE LOOPS
# ----------------------------
print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

# Three Loop Questions:
# 1. What do I want to repeat?
#  -> message
# 2. What do I want to change each time?
#  -> stars
# 3. How long should we repeat?
#  -> 5 times

print('')
i = 0  # iterator
while i < 5:
    print(f'{i+1}.' + '*' * (i+1) + 'Loops are awesome!' + '*' * (i+1))
    i = i + 1
    # i += 1 this is a shorthand form to write the iteration

# ----------------------------
# EXERCISE
# ----------------------------

print('')
print('Guessing game')
print('')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop
# then print to the input box
# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop,
# print to the input box (This is specific to this platform)

correct_number = 76
attempts = 0
attempts_limit = 5
current_attempt = 5
while attempts < attempts_limit:
    guess = int(input(f'Input your guess #{attempts+1}: '))
    if guess == correct_number:
        print(f'You did it! The correct number is {correct_number}')
        break
    else:
        current_attempt -= 1
        print(f'Wrong guess, you have {current_attempt} guesses left')
        attempts += 1

if guess != correct_number:
    print('')
    print('Sorry, you lose...')
    print(f'The correct number is {correct_number}')
