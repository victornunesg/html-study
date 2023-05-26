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
#     if idade > 25 and salarios[i] < media_salario:
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
7. 

Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas
vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de \$3000 em uma semana recebe \$200 mais
9 por cento de \$3000, ou seja, um total de \$470.

Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores: <pre> 
200
−
299 
300
−
399 
400
−
499 
500
−
599 
600
−
699 
700
−
799 
800
−
899 
900
−
999 $1000 em diante
Existem várias formas de fazer. Faça primeiro da forma que parecer mais intuitiva para você.

Em seguida, caso queira um desafio: Desafio: Crie uma forma para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

