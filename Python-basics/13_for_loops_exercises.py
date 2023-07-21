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

# =====================================================================================
# =====================================================================================
# =====================================================================================
# =====================================================================================

"""
1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média
de vendas.
"""

# vendas = [1000, 1500, 1200, 1300]
# vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]
#
# total_vendas = 0
# for i, venda in enumerate(vendas):
#     print(f'Vendedor: {vendedores[i]} / Vendas: {vendas[i]}')
#     total_vendas += vendas[i]
# print(f'\nMedia de vendas: {total_vendas / len(vendas)}')

"""
2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade
de alunos com média maior que 7.
"""

# alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
# notas = [
#     [10, 9, 8, 8],
#     [9, 7, 6, 4],
#     [10, 10, 10, 10],
#     [5, 3, 10, 9],
#     [7, 6, 6, 6],
#     [7, 7, 8, 7],
#     [7, 7, 7, 9],
#     [8, 5, 6, 7],
#     [10, 9, 7, 4],
#     [10, 1, 3, 3],
# ]
#
# medias = []
# aprovados = 0
#
# for nota in notas:
#     if (sum(nota) / len(nota)) >= 7:
#         aprovados += 1
#     medias.append(sum(nota) / len(nota))
#
# for i in range(len(alunos)):
#     print(f'{alunos [i]} - media: {medias[i]}')
# print(f'\nTotal de alunos aprovados: {aprovados}')

"""
3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais 
de 25 anos possuem salário inferior à média de todos os salários.
"""

# idades = [35, 32, 50, 33, 48, 50, 33, 48, 22, 49, 35, 38, 20, 47, 49, 48, 34, 21, 48, 44, 48, 30, 25, 42, 42, 23, 25,
#           23, 38, 35]
# salarios = [3739, 2219, 3554, 3978, 4014, 3270, 4792, 3879, 2981, 2384, 4826, 2460, 3680, 4318, 1872, 1770, 4640, 3929,
#             3295, 1729, 3965, 4267, 4007, 1916, 2987, 2943, 3852, 4543, 2055, 1730]
#
# media_salario = sum(salarios) / len(salarios)
# qtde_func = 0
#
# for i, idade in enumerate(idades):
#     if idade > 25 and (venda * 0.09 + 200) < media_salario:
#         qtde_func += 1
#
# print(f'Temos {qtde_func} funcionarios com mais de 25 anos que recebem menos da media salarial!')

"""
4.Em quais meses a média de temperatura foi maior do que a média nacional?
"""
# meses = [
#     'Janeiro',
#     'Fevereiro',
#     'Março',
#     'Abril',
#     'Maio',
#     'Junho',
#     'Julho',
#     'Agosto',
#     'Setembro',
#     'Outubro',
#     'Novembro',
#     'Dezembro'
# ]
#
# temperaturas = [30, 29, 28, 28, 25, 26, 20, 21, 19, 25, 27, 32]
#
# media = sum(temperaturas) / len(temperaturas)
# print('A media anual foi de {:.2f} graus Celsius'.format(media))
#
# for i, temperatura in enumerate(temperaturas):
#     if temperatura > media:
#         print(f'{meses[i]}, Temperatura: {temperatura} graus Celsius')

"""
5. ABONO SALARIAL

As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado
durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto
será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral,
chegou-se a seguinte forma de cálculo:

. Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
. O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor 
mínimo; 

Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou 
outras particularidades. O programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra
definida acima. Ao final, o programa deverá apresentar:

O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono;

A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos.

Projeção de Gastos com Abono
============================ 

Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0

Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00

Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""

# lista_salarios = [1000, 300, 500, 200, 1500, 3000, 3400, 5000, 7000, 2000, 600, 800, 250, 1500, 20000]
# abonos = []
#
# print('\nProjeção de Gastos com Abono\n============================ ')
# # O salário de cada funcionário, juntamente com o valor do abono;
# print('\nSalário    - Abono   ')
# for i, salarios in enumerate(lista_salarios):
#     if (salarios * 0.2) < 100:
#         abonos.append(100)
#     else:
#         abonos.append(salarios * 0.2)
#     print('R$ {:.2f} - R$ {:.2f}'.format(salarios, abonos[i]))
#
# # O número total de funcionário processados;
# print(f'\nForam processados {len(abonos)} colaboradores.')
#
# # O valor total a ser gasto com o pagamento do abono;
# print('Total gasto com abonos: R$ {:.2f}'.format(sum(abonos)))
#
# # O número de funcionário que receberá o valor mínimo de 100 reais;
# contador = 0
# for abono in abonos:
#     if abono == 100:
#         contador += 1
# print(f'Valor mínimo pago a {contador} colaboradores')
#
# # O maior valor pago como abono;
# print('Maior valor de abono pago: R$ {:.2f}'.format(max(abonos)))

"""
6. RELATÓRIO DE CONSUMO

Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro
de combustível. Calcule e mostre:

a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros
e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. A disposi
ção das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
programa.
"""
# print('Comparativo de Consumo de Combustível')
# veiculos = ['fusca', ' gol', 'uno', 'vectra', 'peugeot']
# autonomias = [7, 10, 12.5, 9, 14.5]
# consumo = []
# despesa = []
#
# for i in range(len(veiculos)):
#     print(f'Veiculo {i+1}\nNome: {veiculos[i]}\nKm por litro: {autonomias[i]} km/l')
#     consumo.append(1000/autonomias[i])
#     despesa.append(consumo[i] * 2.25)
#
# print('Relatório Final')
# for j in range(len(veiculos)):
#     print('{} - {} -  {} - {:.1f} litros - R$ {:.2f}'.format(j+1, veiculos[j], autonomias[j], consumo[j], despesa[j]))
#
# i = consumo.index(min(consumo))
# print(f'O menor consumo é do {veiculos[i]}')

"""
7. COMISSAO DE VENDAS 

Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas
vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de \$3000 em uma semana recebe \$200 mais
9 por cento de \$3000, ou seja, um total de \$470.

Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores: 

200-299 
300−399 
400−499 
500−599 
600−699 
700−799 
800−899 
900−999
$1000 em diante

Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.

Em seguida, caso queira um desafio: Desafio: Crie uma forma para chegar na posição da lista a partir do salário,
sem fazer vários ifs aninhados.
"""
# vendas = [1000, 2000, 3000, 4000, 5000, 6000, 5500, 4500, 3600]
# contadores = [
#     [200, 0],
#     [300, 0],
#     [400, 0],
#     [500, 0],
#     [600, 0],
#     [700, 0],
#     [800, 0],
#     [900, 0],
#     [1000, 0],
# ]
#
# for i, venda in enumerate(vendas):
#     if 200 <= (venda * 0.09 + 200) < 300:
#         contadores[0][1] += 1
#     elif 300 <= (venda * 0.09 + 200) < 400:
#         contadores[1][1] += 1
#     elif 400 <= (venda * 0.09 + 200) < 500:
#         contadores[2][1] += 1
#     elif 500 <= (venda * 0.09 + 200) < 600:
#         contadores[3][1] += 1
#     elif 600 <= (venda * 0.09 + 200) < 700:
#         contadores[4][1] += 1
#     elif 700 <= (venda * 0.09 + 200) < 800:
#         contadores[5][1] += 1
#     elif 800 <= (venda * 0.09 + 200) < 900:
#         contadores[6][1] += 1
#     elif 900 <= (venda * 0.09 + 200) < 1000:
#         contadores[7][1] += 1
#     elif (venda * 0.09 + 200) >= 1000:
#         contadores[8][1] += 1
#
# for i in range(8):
#     print(f'R$ {i+2}00-{i+2}99: {contadores[i][1]}')
