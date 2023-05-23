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

for number in range(8):
    # the variable number is used in 'for' loop to pick each one of the numbers from 0 to 7 to write one by one
    print(number)

print('')
print("For Loop done!")
print('')

for step in range(1, 15, 3):
    # the variable number is used in 'for' loop to pick each one of the numbers from 1 to 15 in steps of 3
    print(step)

print('')
print("For Loop done!")
print('')

for name in ['John', 'Terry', 'Eric', 'Michael', 'George']:
    # the variable number is used in 'for' loop to pick each one of the names in the list above
    print(name)

print('')
print("For Loop done!")
print('')

names = ['John', 'Terry', 'Eric', 'Michael', 'George']
for name in names:
    # the variable number is used in 'for' loop to pick each one of the names in the list names above
    print(name)

produtos = ['coca', 'pepsi', 'guarana', 'sprite', 'fanta']
producao = [15000, 12000, 13000, 5000, 250]

print('Resultado da linha de produção de ontem: \n')
for item in range(len(produtos)):  # gets the total elements using len function to print the information for each one
    print(f'Produto: {produtos[item]} || Produção: {producao[item]} unidades')

print('')
print("For Loop done!")
print('')

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

# Nested loops - a loop inside another loop
friends = ['John', 'Terry', 'Eric']
for friend in friends:
    for number in [1, 2, 3]:
        print(friend, number)

print('')
print("For Loop done!")
print('')

# Enumerate - runs a list and at the same time stores in a variable the index of each item
# you should use only when is necessary to get the list index (because it is slower)

funcionarios = ['José', 'Maria', 'João', 'Pedro', 'Joana', 'Francisca', 'Fernanda', 'Ana', 'Luiz']
for i, funcionario in enumerate(funcionarios):
    print(f'Index {i} é o funcionário {funcionario}')


# ----------------------------
# EXERCISE
# ----------------------------

print('')
print('EXERCISE')
print('')
names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
invitation_list = []
invitation_list.extend(names)
invitation_list.extend(names1)
print(invitation_list)
print('')

invitation_list.append(input('Enter the 1st extra name: '))
invitation_list.append(input('Enter the 2nd extra name: '))
invitation_list = (','.join(invitation_list)).title().split(',')
print(invitation_list, type(invitation_list))
print('')

for invite in invitation_list:
    print(f'{invite}! You are invited to the party on Saturday!')

# =====================================

estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450,
           800]
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça',
            'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte',
            'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
nivel_minimo = 50

for i, qtde in enumerate(estoque):
    if qtde < nivel_minimo:
        print(f'O produto {produtos[i]} está abaixo do nível do estoque mínimo, temos apenas {estoque[i]} unidades')

# =========================================
"""
# Exercícios

## 1. Mudança de Carga Tributária

- Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

Digamos que você trabalhe em uma empresa de ecommerce

No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer quantidade de livros na sua lista.

Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa
"""

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i = produtos.index('livro')
    antigo_total = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    produtos_ecommerce[i][1] = int(produtos_ecommerce[i][1] * 1.1)
    novo_total = produtos_ecommerce[i][0] * produtos_ecommerce[i][1]
    imposto = novo_total - antigo_total
    print(f'O valor do livro subiu para R$ {produtos_ecommerce[i][1]} e o imposto é de R$ {imposto}')
else:
    print('Não há livros nos produtos')
