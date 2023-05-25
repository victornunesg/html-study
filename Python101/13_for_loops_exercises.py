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
#             'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som',
#             'microfone', 'câmera canon']
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


""" 
4. LISTA DE CONVIDADOS

Preenche uma lista de convidados consolidando duas listas distintas;
Adiciona dois convidados extra na lista consolidada;
Arruma os nomes em letra maiúscula e printa no final os convidados separadamente.
"""

# names = ['john ClEEse', 'Eric IDLE', 'michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# invitation_list = []
# invitation_list.extend(names)
# invitation_list.extend(names1)
# print(invitation_list)
# print('')
#
# invitation_list.append(input('Enter the 1st extra name: '))
# invitation_list.append(input('Enter the 2nd extra name: '))
# invitation_list = (','.join(invitation_list)).title().split(',')
# print(invitation_list, type(invitation_list))
# print('')
#
# for invite in invitation_list:
#     print(f'{invite}! You are invited to the party on Saturday!')


"""
5. VERIFICAÇÃO DE ESTOQUE

Verifica quais são os produtos que estão abaixo do estoque mínimo, baseado na comparação entre duas listas que refletem
a lista de produtos e a quantidade atual em estoque.
"""

# estoque = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120,
#            300, 450, 800]
# produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça',
#             'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte',
#             'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
# nivel_minimo = 50
#
# for i, qtde in enumerate(estoque):
#     if qtde < nivel_minimo:
#         print(f'O produto {produtos[i]} está abaixo do nível do estoque mínimo, temos apenas {estoque[i]} unidades')

"""
6. VERIFICAÇÃO DE ESTOQUE (FOR DENTRO DE FOR)

Vamos pegar um exemplo de nível mínimo de estoque. Em uma fábrica você tem vários produtos e não pode deixar que os 
produtos fiquem em falta. Para isso, foi definido uma quantidade mínima de estoque que os produtos precisam ter:

-Identifique quais fábricas tem algum produto abaixo do nível de estoque
-Agora ao invés de analisar o estoque de apenas 1 fábrica, vamos analisar o estoque de várias fábricas

"""
#
# estoque = [
#     [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
#     [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
#     [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
#     [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
#     [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
# ]
# fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
# nivel_minimo = 50
#
# fabricas_alerta = [] # criando lista auxiliar para armazenar as fábricas com estoque baixo
# for i, lista in enumerate(estoque):
#     for qtde in lista:
#         if qtde < nivel_minimo:
#             if fabricas[i] in fabricas_alerta:
#                 pass
#             else:
#                 fabricas_alerta.append(fabricas[i])
# print(fabricas_alerta)

"""
7. CALCULANDO O % DE UMA LISTA

Faremos algo parecido com "filtrar" uma lista. Digamos que a gente tenha uma lista de vendedores e ao invés de saber 
todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. 
Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.

Vamos resolver de 2 formas:
-Criando uma lista auxiliar apenas com os vendedores que bateram a meta
-Fazendo o cálculo diretamente na lista que já temos
-Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?

"""
# meta = 10000
# vendas = [
#     ['João', 15000],
#     ['Julia', 27000],
#     ['Marcus', 9900],
#     ['Maria', 3750],
#     ['Ana', 10300],
#     ['Alon', 7870],
# ]
#
# # Criando uma lista auxiliar apenas com os vendedores que bateram a meta
# meta_batida = []
# for venda in vendas:
#     if venda[1] >= meta:
#         meta_batida.append(venda[0])
# percentual = len(meta_batida) / len(vendas)
# print(f'Lista de vendedores que bateram a meta: {meta_batida}')
# print('Bateram a meta {:.0%} \n'.format(percentual))
#
# # Fazendo o cálculo diretamente na lista que já temos
# contador = 0
# for venda in vendas:
#     if venda[1] >= meta:
#         contador += 1
# percentual2 = contador / len(vendas)
# print(f'Qtde de vendedores que bateram a meta: {contador}')
# print('Bateram a meta {:.0%} \n'.format(percentual2))
#
# # Para treinar uma estrutura parecida, crie um código para responder: quem foi o vendedor que mais vendeu?
# vendedor = '0'
# venda_max = 0
# for venda in vendas:
#     if venda[1] > venda_max:
#         venda_max = venda[1]
#         vendedor = venda[0]
# print(f'O vendedor que mais vendeu: {vendedor}')
# print(f'Quantidade de vendas: {venda_max}')
