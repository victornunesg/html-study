print('\n===========================================================')
print('FUNÇÕES LAMBDA')
print('===========================================================')

""" OBJETVO:

As lambdas expressions são funções anônimas (sem nome mesmo) que tem 1 linha de código e são atribuidas a uma variável,
como se a variável virasse uma função. Elas normalmente são usadas para fazer uma única ação, mas em Python usamos
principalmente dentro de métodos como argumento, para não precisarmos criar uma função só para isso.
Outra aplicação delas está em criar um "gerador de funções".

Permite escrever funções de 1 linha as quais podemos usar uma vez e 'jogar fora'
O valor de retorno é sempre implícito em uma lambda expression, sempre retorna algo (diferente das funções normais)

Obs: Não é "obrigatório" usar lambda expression, até porque praticamente tudo o que você faz com elas você consegue
fazer com functions normais. Mas, é importante saber entender quando encontrar e saber usar a medida que você for se
acostumando e vendo necessidade.

ESTRUTURA: minha_funcao = lambda parametro: expressão """


# # EXEMPLO SIMPLES
# # definindo uma função que retorna um número * 2
# def minha_funcao(num):
#     return num * 2
#
#
# # definindo a mesma função como uma lambda expression:
# minha_funcao2 = lambda num: num * 2
#
# print(minha_funcao2(5))
# print(minha_funcao(5))
#
# # OUTRO EXEMPLO: Usar lambda expressions para criar uma função que calcula o preço dos produtos acrescido do imposto
#
# imposto = 0.3
#
#
# # definindo como função normal:
# def preco_imposto(preco):
#     return preco * (1 + imposto)
#
#
# # definindo como lambda expression:
# preco_imposto2 = lambda preco: preco * (1 + imposto)
#
# print(preco_imposto(100))
# print(preco_imposto2(100))

print('\n===========================================================')
print('PRINCIPAL APLICAÇÃO DE LAMBDA EXPRESSIONS')
print('===========================================================')

# Usar lambda como argumento de alguma outra função, como map e filter

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000,
                    'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

""" FUNÇÃO map(função, iterable)
Retorna um objeto contendo o resultado da função para cada item do iterable

EXEMPLO:
Queremos saber o preço de cada produto adicionando o valor do imposto de 30% sobre o valor do produto """

# imposto = 0.3
#
#
# # utilizando funções convencionais
# def calcular_preco(preco):
#     return preco * 1.3
#
#
# preco_com_imposto = list(map(calcular_preco, preco_tecnologia.values()))
# print(preco_com_imposto)
#
# # utilizando LAMBDA, neste caso não é necessário criar uma function para executar a mesma ação
# # observe que o map dentro de uma lista já retorna a lista pronta
# # mesmo o comando .values() no dicionário, apesar de retornar um dict, quando presente dentro de um list maior, funciona
# preco_com_imposto2 = list(map(lambda preco: preco * (1 + imposto), preco_tecnologia.values()))
# print(preco_com_imposto2)

""" FUNÇÃO filter(função, iterable)
Retorna como resposta todos os itens do iterable onde a função é True

EXEMPLO:
Queremos apenas os produtos que custam acima de 2000 """


# # utilizando funções convencionais (neste caso a função retorna True ou False, para ser usada no filter())
# def maior2000(dicionario):
#     return dicionario[1] > 2000
#
#
# produtos_acima2000 = dict(filter(maior2000, preco_tecnologia.items()))
# print(produtos_acima2000)
#
# # utilizando LAMBDA, neste caso não é necessário criar uma function para executar a mesma ação
# produtos_acima20002 = dict(filter(lambda dici: dici[1] > 2000, preco_tecnologia.items()))
# print(produtos_acima20002)

print('\n===========================================================')
print('LAMBDA EXPRESSIONS PARA GERAR FUNÇÕES')
print('===========================================================')

""" DESCRIÇÃO:
Uma das aplicações de lambda expressions, além do uso em map() e filter(), é criar um "gerador de funções". Nesse caso,
usaremos a lambda expressions dentro da definição de uma outra função.

É menos usado do que a forma anterior que vimos, mas pode ser útil caso queira criar funções que possam ser adaptadas
conforme será descrito a seguir.

EXEMPLO:
Vamos criar uma função que me permita calcular o valor acrescido do imposto de diferentes categorias (produto, serviço,
royalties, etc.) """

# produto 0.1
# serviço 0.15
# royalties 0.25


def calcular_imposto(imposto):  # função que retorna uma lambda expression
    return lambda preco: preco * (1 + imposto)


# definindo as funções que calculam o imposto das 3 categorias (produto, serviço, royalties)
# aqui estamos usando o lambda como construtor de funções
calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.15)
calcular_preco_royalties = calcular_imposto(0.25)

# aplicando um valor de nota fiscal de 100 para ver o resultado
print(int(calcular_preco_produto(100)))
print(int(calcular_preco_servico(100)))
print(int(calcular_preco_royalties(100)))

# # Putting lambda function inside a function:
# def func(n):
#     return n
#
#
# print(type(func(3)))  # in this case will return int
#
#
# # if we put a lambda function as return of a function, the return type will be a function:
#
#
# def func(n):
#     return lambda a: a * n
#     # this function is outputting a new function that is using the 'n' value in that function
#
#
# doubler = func(2)  # doubler is using func to attribute 2 in 'n' variable
# print(doubler(3))  # now we are telling that 'a' variable is 3, returning 6
#
# quintipler = func(5)
# print(quintipler(3))  # getting 15 as return
#
# print(type(func(3)))
#
#
# # Another example of lambda combined with normal functions
# # A function to calculate a price based on a start-up cost and an hourly cost
#
#
# def price_calc(start, hourly_rate):
#     return lambda hours: start + hourly_rate * hours
#
#
# # price for a regular customer, 10 dollars start-up fee and 30 dollars as hourly cost
#
#
# walking_cost = price_calc(10, 30)
# print(walking_cost(2))  # calculating 2 hours of treatment for a regular customer
#
# premium_cost = price_calc(1, 25)
# print(premium_cost(2))  # calculating 2 hours of treatment for a premium customer
#
# # call the function immediately
# print(price_calc(1, 25)(2))  # same result as previous example
#
# # other examples calling a lambda immediately, using default values and specifying them
# print((lambda a, b, c: a + b + c)(2, 3, 4))  # calling immediately
# print((lambda a, b, c=2: a + b + c)(2, 3))  # using default values
# print((lambda a, b, c: a + b + c)(a=2, c=3, b=4))  # specifying arguments (does not matter the order in this case)
# print((lambda *args: sum(args))(2, 3, 4, 50))  # unpacking arguments
#
# # ----------------------------
# # EXERCISE
# # ----------------------------
# print('\nExercise\n')
# # Writing equivalent lambda functions for the previous ones
#
# # def f(x): return x + 5
# f = lambda x: x + 5
# print(f(2))
#
# # def strip_spaces(str):
# #   return ''.join(str.split(' '))
# strip_spaces1 = lambda x: ''.join(x.split(' '))  # write equivalent lambda and insert Lambda here
# print(strip_spaces1('Monty Pythons Flying Circus'))
#
# # def join_list_no_duplicates(list_a,list_b):
# #    return list(set(list_a + list_b))
# list_a = [1, 2, 3, 4]
# list_b = [3, 4, 5, 6, 7]
# # print(join_list_no_duplicates(list_a,list_b))
# join_list_no_duplicates1 = lambda x, y: list(set(x + y))
# print(join_list_no_duplicates1(list_a, list_b))
#
#
# # Complete the function so it returns a function
#
#
# def create_quad_func(a, b, c):
#     '''return function f(x) = ax^2 + bx + c'''
#     return lambda x: (a * (x ** 2)) + (b * x) + c
#
#
# f = create_quad_func(2, 4, 6)
# g = create_quad_func(1, 2, 3)
# print(f(2))
# print(g(2))
#
# signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
# # Lexicographic sort (without considering the integer as the main point to sort it)
# print(sorted(signups))
# # write sorting by integer
# print(sorted(signups, key=lambda id: int(id[3:])))  # Integer sort
#
#
# class Player:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# Eric = Player('Eric', 116700)
# John = Player('John', 24327)
# Terry = Player('Terry', 150000)
# player_list = [Eric, John, Terry]
#
# # Exercise: Sort this by score using lambda!
# player_list.sort(key=lambda playyer: playyer.score)  # order by score
# print([player.name for player in player_list])
# player_list.sort(key=lambda playyer: playyer.score, reverse=True)  # top score first
# print([player.name for player in player_list])
