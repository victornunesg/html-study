print('\n===========================================================')
print('LIST COMPREHENSION')
print('===========================================================')

""" 
List Comprehension é uma forma de iterar pelos elementas das listas de maneira "mais direta", com mais "cara de Python"
Permite a criação de listas, sets, dicionários com menos código (em uma linha só)
Tudo ue você faz com list comprehension pode ser feito com loop FOR, pois elas contém o mesmo código

ESTRUTURA:
lista = [expressão for item in iterable]
"""

# preco_produtos = [100, 150, 300, 5500]
# produtos = ['vinho', 'cafeiteira', 'microondas', 'iphone']
#
# #digamos que o imposto sobre os produtos é de 30%, ou seja, 0.3. Como eu faria para criar uma lista com os
# #valores de imposto de cada produto?
#
# # usando o FOR
# impostos = []
# for item in preco_produtos:
#     impostos.append(item * 0.3)
# print(impostos)
#
# # usando LIST COMPREHENSION
# impostos = [preco * 0.3 for preco in preco_produtos]
# print(impostos)
#
#
# # a "expressão" na list comprehension pode ser uma function tb
# def calcular_imposto(preco, imposto):
#     return preco * imposto
#
#
# impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]
# print(impostos)

""" OBSERVAÇÃO:
Normalmente isso é usado quando queremos fazer uma única ação com os itens de uma lista. Não é obrigatório, mas é comum
de encontrar principalmente com programadores mais experientes/preocupados com "a melhor forma de fazer alguma coisa"

Cuidado: se a sua lista for MUITO grande, o list comprehension pode acabar sendo difícil de compilar. Nesses casos
podemos usar funções, for tradicionais com breaks para interromper ou até bibliotecas como o panda que trabalham bem com
muitos dados.
"""

# EXEMPLO PRÁTICO - ordenando duas listas relacionadas (do maior valor para o menor valor)
vendas_itens = [1500, 150, 2100, 1950]
itens = ['vinho', 'cafeiteira', 'microondas', 'iphone']

lista_aux = list(zip(vendas_itens, itens))  # transformando as duas listas em uma lista de tuplas com o ZIP
lista_aux.sort(reverse=True)  # ordenando as tuplas do maior para o menor valor de vendas
produtos = [produto for vendas, produto in lista_aux]  # list comprehension para atualizar a lista de produtos
print(produtos)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # give me a list with num for each num in numbers if num is even
# new_list = [num for num in numbers if num % 2 == 0]
# print('\n', new_list)
#
# # using filter and lambda function to do it: (more complicated)
# new_list = filter(lambda num1: num1 % 2 == 0, numbers)
# print('\n', list(new_list))  # filter will bring an object filtered, so we must turn into a list
#
# # Other exemple: I want a (letter, num) pair for each letter in 'spam' and each number in '0123'
# new_list = []
# for letter in 'spam':
#     for num in range(4):
#         new_list.append((letter, num))
# print('\n', new_list)
#
# # doing the same thing as for loop above using comprehensions, with less code:
# new_list = [(letter, num) for letter in 'spam' for num in range(4)]
# print('\n', new_list)
#
# # ----------------------------
# # COMPREHENSIONS - DICTIONARIES
# # ----------------------------
# print('\n Comprehensions - Dictionaries')
# print('----------------------')
#
# # Dictionary comprehensions
# movies = ["And Now for Something Completely Different", "Monty Python and the Holy Grail",
#           "Monty Python's Life of Brian", "Monty Python Live at the Hollywood Bowl",
#           "Monty Python's The Meaning of Life", "Monty Python Live (Mostly)"]
# year = [1971, 1975, 1979, 1982, 1983, 2014]
# names = ['John', 'Eric', 'Michael', 'Graham', 'Terry', 'TerryG']
#
# # create a list containing movies and year
# print('\n', list(zip(movies, year)))  # combined as tuples inside a list
#
# # give me a dict('movies': year) for each movie, year in zip(movies, year)
# # using for loop - option #1
# movies2 = {}
# for movie in (list(zip(movies, year))):
#     movies2.update(list(zip(movies, year)))
# print('\n', movies2)
#
# # using for loop - option #2
# movies2 = dict()
# for movie, yr in zip(movies, year):
#     movies2[movie] = yr
# print('\n', movies2)
#
# # now using comprehensions to do the same stuff
# movies2 = {movie: yr for movie, yr in zip(movies, year)}
# print('\n', movies2)
#
# # getting the movies before 1983 starting with 'Monty' (adding if clause)
# movies2 = {movie: yr for movie, yr in zip(movies, year) if yr < 1983 and movie.startswith('Monty')}
# print('\n', movies2)
#
# # now we want to create a dict with name + movie + year:
# n1 = [[name + "s favorite movie was '" + movie + "' from " + str(yr)] for name, movie, yr in zip(names, movies, year)
#       if yr < 1981]
# print('\n', n1)
