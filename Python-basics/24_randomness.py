# ----------------------------
# RANDOMNESS
# ----------------------------
import random, string

for i in range(5):
    print(type(random.randint(0,10)))  # now creating 5 different random numbers up to 6
print('\n')

print('\n Randomness')
print('----------------------')
# when working with randomness we import the random module, but is not truly random (like a sudo randomness)
# when you want to do really secure randomness generation, you need to use other python modules

print(random.random())  # this function generates number between 0 and 1 (but not 1)
print('\n')

for i in range(5):
    print(random.random() * 6)  # now creating 5 different random numbers up to 6
print('\n')

# another way of doing that is using 'uniform' function, where you specify the random number range
for i in range(5):
    print(random.uniform(1, 6))  # now creating 5 different random numbers up to 6
print('\n')

# now using 'randint' to get random integer numbers between 1 and 6
for i in range(5):
    print(random.randint(1, 6))
print('\n')

# getting random numbers between 1 and 100 in steps of 2 (1,3,5,...) using 'randrange' function
for i in range(5):
    print(random.randrange(1, 100, 2))
print('\n')

# getting a random name from a list of names using 'choice' function
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))
print('\n')

# getting a random sample from a list of names using 'sample' function and specifying number of samples
# this function will not bring duplicate values, for example, will not bring 'John' twice. to do it, use 'choices'
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list, 3))
random.shuffle(friends_list)  # changing list order in a random way, using 'shuffle' function (works with lists and num)
print(friends_list)
print('\n')

# now it is an example to be used when creating passwords, random strings
# we are importing string module since contains constants that holds pre-defined string values
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

letters_numbers = string.ascii_letters + string.digits  # creates string based in small/large caps letters and digits
print('\n', letters_numbers)

word = ''
for i in range(7):
    word += random.choice(letters_numbers)  # generates a random string with letters and digits of 7 characters
    # in this way we can have repeated characters considering we are using 'choice' function
print('\n', word)

# this also generates a 7 char string but no duplicates char
word1 = ''.join(random.sample(letters_numbers, 7))
print('\n', word1)

# using 'choices' function is not necessary to use join, but can bring duplicated chars
word2 = random.choices(letters_numbers, k=7)
print('\n', word2)
