# ----------------------------
# FOR LOOPS
# ----------------------------

print('')
print('For loops')
print('')

# In for loops we already know how many interactions will be performed in advance
for letter in 'Norwegian blue':  # 'letter' is the variable
    # the variable letter is used in 'for' loop to pick each one of characters in the string to write one by one
    print(letter)  # now the letters are getting printed one by one

print('')
print("For Loop done!")
print('')

###################################

for number in range(8):
    # the variable number is used in 'for' loop to pick each one of the numbers from 0 to 7 to write one by one
    print(number)

print('')
print("For Loop done!")
print('')

###################################

for step in range(1, 15, 3):
    # the variable number is used in 'for' loop to pick each one of the numbers from 1 to 15 in steps of 3
    print(step)

print('')
print("For Loop done!")
print('')

###################################

for name in ['John', 'Terry', 'Eric', 'Michael', 'George']:
    # the variable number is used in 'for' loop to pick each one of the names in the list above
    print(name)

print('')
print("For Loop done!")
print('')

###################################

names = ['John', 'Terry', 'Eric', 'Michael', 'George']
for name in names:
    # the variable number is used in 'for' loop to pick each one of the names in the list names above
    print(name)

###################################

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

print('Resultado da linha de produção de ontem: \n')
for item in range(len(produtos)):  # gets the total elements using len function to print the information for each one
    print(f'Produto: {produtos[item]} || Produção: {producao[item]} unidades')

print('')
print("For Loop done!")
print('')

###################################

# Break and Continue statements (For Each)
friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        break  # in this case it will find John, Terry and Eric and will jump out of the loop afterwards
    print(friend)

print('')
print("For Loop done!")
print('')

###################################

friends = ['John', 'Terry', 'Eric', 'Michael', 'George']
for friend in friends:
    if friend == 'Eric':
        print('Found' + friend + '!')
        continue  # in this case it will find John, Terry and Eric and will continue the others
        # continues inside the for loop
    print(friend)

print('')
print("For Loop done!")
print('')

###################################

# NESTED LOOPS - a loop inside another loop

friends = ['John', 'Terry', 'Eric']
for friend in friends:
    print(friend) # this code will be executed 3 times since friends list has 3 elements only
    for number in [1, 2, 3]:  # the variables needs to be different in each for loop
        # this code will be executed 3 x 3 times, because there are 3 elements in each list of for loop
        print(friend, number)

print('')
print("For Loop done!")
print('')

###################################

# ENUMERATE

# runs a list and at the same time stores in a variable the index of each item
# you should use only when is necessary to get the list index (because it is slower)

funcionarios = ['José', 'Maria', 'João', 'Pedro', 'Joana', 'Francisca', 'Fernanda', 'Ana', 'Luiz']
for i, funcionario in enumerate(funcionarios):
    print(f'Index {i} é o funcionário {funcionario}')

###################################

# BREAK AND CONTINUE

vendas = [100, 150, 1500, 2000, 120]
vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']

# Break: interrupts and finishes for loop, it goes to the next line outside for loop
meta = 110
for venda in vendas:
    if venda < meta:
        print('A loja não ganha bônus')
        break
    print(venda)  # não será executado

# Continue: interrupts and goes to the next item inside for loop
meta = 130
for venda in vendas:
    if venda < meta:
        continue
    print(venda)  # imprime somente os casos onde a venda > meta
