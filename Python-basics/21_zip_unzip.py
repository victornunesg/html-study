# ----------------------------
# ZIP AND UNZIP
# ----------------------------

# Combine iterables: strings, tuples, lists, etc

nums = '1234'
letters = ['a', 'b', 'c', 'd']
names = ['John', 'Eric', 'Michael', 'Graham', 'Joe']

combo = zip(nums, letters)
print(combo)  # prints a zip object, need to transform it to see the content

combo = list(zip(nums, letters, names))  # you can transform into a dict (until 2 items) or a tuple
print(combo)

# you can unzip and put the result into variables:
num, let, nam = zip(*combo)
print(num)
print(let)
print(nam)

# other example creating a dictionary from 2 strings
keys = 'this parrot is deceased'
values = 'denna papegojan är avliden'

# considering the spaces between words, it is better to turn into a list first
keys = keys.split()
values = values.split()
print(keys, values)
translation = dict(zip(keys, values))
print(translation)

# other way to do the same thing using comprehension
new_dict = {key: value for key, value in zip(keys, values)}
print(new_dict)

# now if we want to take the dictionary apart
reverse = list(translation.keys()), list(translation.values())
print(reverse)

# other way to do the same thing using unzip
reverse1 = list(zip(*translation.items()))
print(reverse1)
