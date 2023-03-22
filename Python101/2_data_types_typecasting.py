# ----------------------------
# DATA TYPES & TYPECASTING
# ----------------------------

print('--------------------------------')
print('Data types and typecasting')
print('--------------------------------')
print('')
# Variables has to be defined in one word, using underscores and not using capitalization
failed_subjects = 2  # integer
name = 'John'  # string
price = 2.45  # float
is_going_to_party = True  # boolean
a = 'it\'s'  # we use backslash to tell Python that the next character needs to be included in the string
print(a)
print(type(failed_subjects))
print(type(name))
print(type(price))
print(type(is_going_to_party))
print('')

# Typecasting is used to change a variable type in an explicit way:
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
print('')

a = int(1)         # 'a' will be 1
b = int(2.5)       # b will be 2
c = int("3")       # c will be 3
c1 = int(float("3.4"))   # Is necessary to first change into float to change it to an integer after
d = float(1)       # d will be 1.0
e = float(2.5)     # e will be 2.5
f = float("3")     # f will be 3.0
g = float("4.23")  # g will be 4.23
h = str("80s")     # h will be 80s
i = str(22)        # 'i' will be 22
j = str(3.01)      # j will be '3.01'

print([a, b, c, c1, d, e, f, g, h, i, j])
print('')
