# ----------------------------
# LAMBDA FUNCTIONS
# ----------------------------
print('\nLambda (anonymous) Functions')

# allows you to write single-line function definitions that you might use once and throw away
# the return value is implicit in a lambda function (ALWAYS) so always returns a value (different from normal funcions)


# normal function definition:
def square(x):
    return x*x


print(square(3))

# Lambda function definition:
# name = lambda parameter(s): expression
square1 = lambda x: x*x

print(square1(3))

# Putting lambda function inside a function:


def func(n):
    return n


print(type(func(3)))  # in this case will return int

# if we put a lambda function as return of a function, the return type will be a function:


def func(n):
    return lambda a: a * n
    # this function is outputting a new function that is using the 'n' value in that function


doubler = func(2)  # doubler is using func to attribute 2 in 'n' variable
print(doubler(3))  # now we are telling that 'a' variable is 3, returning 6

quintipler = func(5)
print(quintipler(3))  # getting 15 as return

print(type(func(3)))

# Another example of lambda combined with normal functions
# A function to calculate a price based on a start-up cost and an hourly cost


def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours

# price for a regular customer, 10 dollars start-up fee and 30 dollars as hourly cost


walking_cost = price_calc(10, 30)
print(walking_cost(2))  # calculating 2 hours of treatment for a regular customer

premium_cost = price_calc(1, 25)
print(premium_cost(2))  # calculating 2 hours of treatment for a premium customer

# call the function immediately
print(price_calc(1, 25)(2))  # same result as previous example

# other examples calling a lambda immediately, using default values and specifying them
print((lambda a, b, c: a+b+c)(2, 3, 4))  # calling immediately
print((lambda a, b, c=2: a+b+c)(2, 3))  # using default values
print((lambda a, b, c: a+b+c)(a=2, c=3, b=4))  # specifying arguments (does not matter the order in this case)
print((lambda *args: sum(args))(2, 3, 4, 50))  # unpacking arguments

# ----------------------------
# EXERCISE
# ----------------------------
print('\nExercise\n')
# Writing equivalent lambda functions for the previous ones

# def f(x): return x + 5
f = lambda x: x+5
print(f(2))

# def strip_spaces(str):
#   return ''.join(str.split(' '))
strip_spaces1 = lambda x: ''.join(x.split(' '))  # write equivalent lambda and insert Lambda here
print(strip_spaces1('Monty Pythons Flying Circus'))


# def join_list_no_duplicates(list_a,list_b):
#    return list(set(list_a + list_b))
list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]
# print(join_list_no_duplicates(list_a,list_b))
join_list_no_duplicates1 = lambda x, y: list(set(x + y))
print(join_list_no_duplicates1(list_a, list_b))

# Complete the function so it returns a function


def create_quad_func(a,b,c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: (a*(x**2)) + (b*x) + c


f = create_quad_func(2, 4, 6)
g = create_quad_func(1, 2, 3)
print(f(2))
print(g(2))


signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# Lexicographic sort (without considering the integer as the main point to sort it)
print(sorted(signups))
# write sorting by integer
print(sorted(signups, key=lambda id: int(id[3:])))  # Integer sort


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

# Exercise: Sort this by score using lambda!
player_list.sort(key=lambda playyer: playyer.score)  # order by score
print([player.name for player in player_list])
player_list.sort(key=lambda playyer: playyer.score, reverse=True)  # top score first
print([player.name for player in player_list])

