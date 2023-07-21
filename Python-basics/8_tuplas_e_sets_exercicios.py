"""
1. Verifique se 'Eric’ e ‘John’ existem em friends
2. Combine ou adicione os dois sets
3. Encontre nomes que estejam em ambos os sets
4. Encontre nomes que estejam somente em friends
5. Mostre apenas os nomes que aparecem somente em uma das listas
6. Crie uma nova cars-list sem duplicados
"""

# friends = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
# my_friends = {'Reg', 'Loretta', 'Colin', 'John', 'Graham'}
# cars = ['900', '420', 'V70', '911', '996', 'V90', '911', '911', 'S', '328', '900']
# john = {'John', 'Eric'}
#
# # 1. Check if ‘Eric’ and ‘John’ exist in friends
# print(friends.intersection(john))
# print('Eric' in friends and 'John' in friends)
#
# # 2. combine or add the two sets
# print('')
# print(friends.union(my_friends))
# print(friends | my_friends)  # other way to union sets
#
# # 3. Find names that are in both sets
# print('')
# print(friends.intersection(my_friends))
# print(friends & my_friends)  # other way to get the intersection between sets
#
# # 4. find names that are only in friends
# print('')
# print(friends.difference(my_friends))
# print(friends - my_friends)  # other way to get the difference between sets
#
# # 5. Show only the names who only appear in one of the lists
# print('')
# print(my_friends.symmetric_difference(friends))
# print(my_friends ^ friends)  # other way to get only the results that does not repeat between sets
#
# # 6. Create a new cars-list without duplicates
# cars_new = set(cars)  # now we created a set of cars without duplicated values
# cars_new = list(set(cars))  # and now we turned back into a list, without duplicated values
# print(cars)
# print(cars_new)

"""
Digamos que você está analisando as vendas do Banco de Dados de um e-commerce.
Em um determinado dia, você extraiu as vendas do Banco de Dados e elas vieram no formato a seguir

Qual foi o faturamento de IPhone no dia 20/08/2020?
Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?
"""

# vendas = [
#     ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
#     ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
#     ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
#     ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
#     ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
#     ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
#     ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
#     ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
# ]
#
# faturamento = 0
# qtde = 0
# mais_vendido = ''
# detalhe = ''
# for item in vendas:
#     # print(item)  # retorna cada tupla da lista de vendas
#     data, produto, cor, capacidade, unidades, valor_unitario = item  # unpacking em variáveis
#     if produto == 'iphone x' and data == '20/08/2020':
#         faturamento += unidades * valor_unitario
#     if data == '21/08/2020':
#         if unidades > qtde:
#             qtde = unidades
#             mais_vendido = produto
#             detalhe = capacidade
#
# print(f'Faturamento de iPhone em 20/08/2020: R$ {faturamento:.2f}')
# print(f'Produto mais vendido em 21/08/2020: {mais_vendido} {detalhe} - {qtde} unidades')

"""
1. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que
bateram a meta e qual foi o valor que eles venderam.
"""

# meta = 10000
# vendas = [
#     ('João', 15000),
#     ('Julia', 27000),
#     ('Marcus', 9900),
#     ('Maria', 3750),
#     ('Ana', 10300),
#     ('Alon', 7870),
# ]
#
# print('Vendedores que bateram a meta:\n')
# for vendedor, venda in vendas:  # dá para fazer o unpacking dentro do próprio for, como um enumerate
#     if venda > meta:
#         print(f'{vendedor}, com {venda} vendas.')

"""
2. Comparação com Ano Anterior
Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano
de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020
para 2019. 

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer:
(vendas_produto2020/vendas_produto2019 - 1)

A lógica da tupla é: (produto, vendas2019, vendas2020)
"""
# vendas_produtos = [
#     ('iphone', 558147, 951642),
#     ('galaxy', 712350, 244295),
#     ('ipad', 573823, 26964),
#     ('tv', 405252, 787604),
#     ('máquina de café', 718654, 867660),
#     ('kindle', 531580, 78830),
#     ('geladeira', 973139, 710331),
#     ('adega', 892292, 646016),
#     ('notebook dell', 422760, 694913),
#     ('notebook hp', 154753, 539704),
#     ('notebook asus', 887061, 324831),
#     ('microsoft surface', 438508, 667179),
#     ('webcam', 237467, 295633),
#     ('caixa de som', 489705, 725316),
#     ('microfone', 328311, 644622),
#     ('câmera canon', 591120, 994303)
# ]
#
# print('Comparação 2020 vs 2019 - Crescimento de vendas\n')
# for venda in vendas_produtos:
#     produto, vendas2019, vendas2020 = venda
#     if vendas2020 > vendas2019:
#         print(f'Produto: {produto} - Vendas 2019: {vendas2019} unidades - Vendas 2020 {vendas2020} unidades - '
#               f'{(vendas2020/vendas2019 - 1):.2%}')
