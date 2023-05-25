# File to practice - EXERCISES

"""
1. REGISTRO DE HÓSPEDES

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem
ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

    1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input),

    2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada
    pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome),

    3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista
    é o nome da pessoa e o cpf da pessoa, assim:

    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],

Para simplificar, não vamos nos preocupar com possibilidades de tentar colocar mais de 1 hóspede, digitar o cpf errado,
etc. Nosso objetivo é treinar a criação de uma rotina de cadastro.
"""

# qtde_pessoas = int(input('Insira o total de pessoas a serem acomodadas (1 a 4): '))
# hospede = []
# quarto = []
#
# for i in range(qtde_pessoas):
#     nome = input(f'Nome do hóspede {i+1}: ')
#     cpf = input(f'CPF do hóspede {i+1}: ')
#     hospede = [nome, f'CPF: {cpf}']
#     quarto.append(hospede)
#
# print('Informações do quarto:')
# print(hospede)
# print(quarto)

"""
2. ANÁLISE DE VENDAS

Nesse exercício vamos fazer uma análise simples de atingimento de Meta.
Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que 
bateram a meta e qual foi o valor que eles venderam.

"""

# meta = 10000
# vendas = [
#         ['João', 15000],
#         ['Julia', 27000],
#         ['Marcus', 9900],
#         ['Maria', 3750],
#         ['Ana', 10300],
#         ['Alon', 7870],
# ]
#
#
# for item in vendas:
#     if item[1] >= meta:
#         print(f'O vendedor {item[0]} bateu a meta, vendeu {item[1]} unidades')

"""
3. COMPARAÇÃO COM ANO ANTERIOR

Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano 
de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 
para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: 
(vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu for
"""

# produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell',
#             'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
# vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139, 892292, 422760, 154753, 887061, 438508, 237467,
#               489705, 328311, 591120]
# vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331, 646016, 694913, 539704, 324831, 667179, 295633,
#               725316, 644622, 994303]
#
# for i, produto in enumerate(produtos):
#     if vendas2020[i] > vendas2019[i]:
#         print(f'Produto: {produtos[i]}, Vendas 2019: {vendas2019[i]}, Vendas 2020: {vendas2020[i]}')
#         print(f'Percentual de crescimento: {vendas2020[i] / vendas2019[i] - 1} %')
#         print('\n')
