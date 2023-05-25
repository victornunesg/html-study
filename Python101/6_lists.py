# ----------------------------
# LISTS
# ----------------------------
print('--------------------------------')
print('Lists')
print('--------------------------------')

# Very similar to variables
# Can storage multiple data and mix different types of data

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
#  index:    0         1         2       3         4
print(friends[2])  # printing 'Terry'
print(friends[-1])  # printing Graham
print(friends[2:4])  # will not print 'Graham'
print(friends[:])  # hole list
print(len(friends))  # checking how many elements this list has
print(friends.index('Eric'))  # checking in what position one element is
print(friends.count('Eric'))  # checking how many occurrences one element has in the list

# sorting a list
print('')
print(friends)
friends.sort()  # sorts in crescent order, it is case sensitive, upper case letters are ordered first
print(friends)
friends.sort(reverse=True)  # sorts in decreasing order
print(friends)
friends.reverse()  # reverses the order of the original string
print(friends)

cars = [911, 130, 328, 535, 740, 308]
print('')
print(min(cars))  # lowest number in the list
print(max(cars))  # highest number in the list
print(sum(cars))  # sum work with numbers only
print(min(friends))  # alphabetic order
print(max(friends))  # alphabetic order

# add elements in a list
print('')
friends.append('TerryG')  # adding an element at the end of the list
print(friends)
friends.insert(1, 'Victor')  # specifying in which position we want to add an element

# changing/updating a list element
print(friends)
friends[0] = 'William'  # changed the value of the 0 position
print(friends)

# removing elements from a list
friends.remove('Terry')  # just remove a list item, the item name needs to be specified
friends.pop(2)  # index needs to be specified. By default removes the last item in the list. Different from remove,
# using pop you release memory in the program and you can store into a variable the item you popped from the list:
removed_item = friends.pop(3)
# friends.clear()  # empty list
# del friends  # now the list is gone
del cars[2]  # removing index 2 from the list

# extend lists, merge them
print('')
friends.extend(cars)  # using extend method, you edit your original list
new_list = friends + cars  # in this way you create a new list, containing two other lists together
print(friends)
# append method can't be used to mix lists, if you do it, the first list will contain the second list inside,
# it will not add the items properly

# copying lists
print('')
# if you do: 'list1 = list2' does not have the same effect, in this case you will get 2 variables referring to the same
# list so if you change one, the other will also be impacted
# the proper way to do it is:
new_cars = cars[:]
# new_cars = cars.copy()  # does the same thing as the line above
# new_cars = list(cars)  # does the same thing as the line above
print(cars)
print(new_cars)


# Exercise - lemonades
sales_w1 = [7, 3, 42, 19, 15, 35, 9]
sales_w2 = [12, 4, 26, 10, 7, 28]
sales = []

# Getting the number of the last day of sell - 1st option
sales_w2.append(int(input('Inform the number of lemonades sold in the last day: ')))

# Getting the number of the last day of sell - 2nd option
new_day = input('Enter #of lemonades for new day: ')
sales_w2.append(int(new_day))

# Combining the 2 lists to put in sales list - 1st option
sales.extend(sales_w1)
sales.extend(sales_w2)

# Combining the 2 lists to put in sales list - 2nd option
sales = sales_w1 + sales_w2
sales.sort()

# Combining the 2 lists to put in sales list - 3rd option
sales = [x + y for x, y in zip(sales_w1, sales_w2)]

print(sales_w1)
print(sales_w2)
print(sales)
print('')

worst_day_prof = sales[0] * 1.5
best_day_prof = sales[-1] * 1.5

print(f'Best day: Separately = {max(max(sales_w1), max(sales_w2))} // General: {max(sales)}')
print(f'Worst day: Separately = {min(min(sales_w1), min(sales_w2))} // General: {min(sales)}')

print(f'Worst day profit:$ {worst_day_prof}')
print(f'Best day profit:$ {best_day_prof}')
print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# Nested lists - listas de listas
vendedores = ['Lira', 'João', 'Diego', 'Alon']
produtos = ['ipad', 'iphone']
vendas = [
    [100, 200],
    [300, 500],
    [50, 1000],
    [900, 10],
]

# - Quanto João vendeu de IPad?
vendas_ipad_joao = vendas[1][0]
print(f'Vendas de iPad do João: {vendas_ipad_joao} unidades.')

# - Quanto Diego vendeu de IPhone
vendas_iphone_diego = vendas[2][1]
print(f'Vendas de iPhone do Diego: {vendas_iphone_diego} unidades.')

# - Qual o total de vendas de IPhone e de IPad?
vendas_ipad = vendas[0][0] + vendas[1][0] + vendas[2][0] + vendas[3][0]
print(f'Vendas de iPad no total: {vendas_ipad}')
vendas_iphone = vendas[0][1] + vendas[1][1] + vendas[2][1] + vendas[3][1]
print(f'Vendas de iPhone no total: {vendas_iphone}')

# - E se Lira na verdade fez apenas 50 vendas de IPhone, como eu modifico na minha lista o valor de vendas dele?
print(vendas)
vendas[0][1] = 50
print(vendas)

# - E se agora eu tenho um novo produto 'mac', como eu adiciono as vendas em cada um dos vendedores?
print(produtos)
print(vendas)

vendas_mac = [10, 15, 6, 70]
produtos.append('mac')

vendas[0].append(vendas_mac[0])
vendas[1].append(vendas_mac[1])
vendas[2].append(vendas_mac[2])
vendas[3].append(vendas_mac[3])

print(produtos)
print(vendas)

# to manage possible errors, besides using an if clause, we can use try/except
# then, the code will be executed but if an error comes up, the except block will be executed
try:
    sales_w1.remove('ZZ')
except:
    print('ZZ could not be removed')

"""

Métodos Específicos de Lista em Python

- list.append(valor)<br>
Adiciona um valor ao final de uma lista

Uso:
    vendas = [150, 320]
    vendas.append(110)
Resultado:
    vendas = [150, 320, 110]

- list.extend(lista2)<br>
Adiciona todos os valores da lista2 na lista original

Uso:
    vendas = [150, 320, 110, 450, 390, 370]
    vendas_2semestre = [440, 470, 900, 1000, 1100, 1050]
    vendas.extend(vendas_2semestre)
Resultado:
    vendas = [150, 320, 110, 450, 390, 370, 440, 470, 900, 1000, 1100, 1050]

- list.insert(posicao, valor)<br>
Adiciona um valor em uma posição específica em uma lista. Não é recomendado usar a não ser que seja realmente necessário inserir em uma posição específica, porque o método append é mais eficiente.

Uso:
    vendas = [150, 320]
    vendas.insert(1, 110)
Resultado:
    vendas = [150, 110, 320]
Obs:
    Compare com o caso do list.append para ver a diferença

- list.remove(valor)<br>
Remove o valor da lista (apenas a 1ª ocorrência, então caso haja 2 vezes o valor na lista, apenas a 1ª será removida). Além disso, dá um erro caso valor não exista dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.remove('Maria')
Resultado:
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.pop(posicao)<br>
Remove o item que está na posicao (índice) passado. Além disso, esse item é dado como resultado do pop, portanto pode ser armazenado em uma variável ou usado para outra coisa na mesma linha de código.

Uso:<br>
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']<br>
    vendedores.pop(2)<br>
Resultado:<br>
    vendedores = ['João', 'Julia', 'Ana', 'Paulo', 'Marcus']

- list.clear()<br>
Remove todos os itens de uma lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    vendedores.clear()
Resultado:
    vendedores = []

- list.index(valor)<br>
Retorna a posição do valor dentro da lista (em qual índice está o valor). Dá erro caso não haja o valor dentro da lista.

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus']
    posicao_Joao = vendedores.index('João')
Resultado:
    posicao_Joao = 0

- list.count(valor)<br>
Retorna a quantidade de vezes que o valor aparece na lista

Uso:
    vendedores = ['João', 'Julia', 'Maria', 'Ana', 'Paulo', 'Marcus', 'João']
    qtde_Joao = vendedores.count('João')
Resultado:
    qtde_Joao = 2

- list.sort(reverse=False)<br>
Ordena os valores da lista em ordem crescente, ou alfabética, (reverse=False) ou decrescente (reverse=True).

Uso:
    vendas = [150, 300, 190, 480]
    vendas.sort(reverse=True)
Resultado:
    vendas = [480, 300, 190, 150]

- list.reverse()<br>
Inverte a ordem dos elementos de uma lista.

Uso:
    vendas = [150, 300, 190, 480]
    vendas.reverse()
Resultado:
    vendas = [480, 190, 300, 150]

- list.copy()<br>
Cria uma cópia da lista original. Outra opção é fazer lista2 = lista1[:]

Uso:
    vendas = [150, 300, 190, 480]
    vendas2 = vendas.copy()
Resultado:
    vendas2 = [150, 300, 190, 480]
"""


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