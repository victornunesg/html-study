"""
Crie um programa que funcione como o registro de vendas de uma empresa.
Nele, a pessoa deve inserir o nome do produto e o produto deve ser adicionado na lista de venda.
Enquanto o usuário não encerrar o programa, significa que ele está registrando novos produtos, então o programa deve
permitir e entrada de quantos produtos o usuário quiser.
"""

# print('Registre um produto.\nPara cancelar o registro de um novo produto, basta apertar enter com a caixa vazia')
#
# vendas = []
# venda = input('\nDigite o nome do produto:')
# while venda != "":
#     vendas.append(venda)
#     venda = input('\nDigite o nome do produto:')
#
# print('Registro Finalizado. As vendas cadastradas foram: {}'.format(vendas))

"""
Vamos criar um sistema de vendas. Nosso programa deve registrar os produtos e as quantidades (2 inputs) e adicionar em
uma lista. O programa deve continuar rodando até o input ser vazio, ou seja, o usuário apertar enter sem digitar nenhum
produto ou quantidade.

Ao final do programa, ele deve printar todos os produtos e quantidades vendidas.

Obs: Caso queira, para o print ficar mais visual, pode usar o join para cada item ser printado em uma linha.

Podemos fazer o While de 2 maneiras:
1. While com a condição que finalize o programa
2. While rodando para sempre, mas com uma condição dentro do while que dê um break no código.
"""

# # Melhor resposta:
# vendas = []
#
# while True:
#     produto = input('Insira o nome do produto: ')
#     if not produto:
#         break
#     qtde = int(input('Insira a quantidade: '))
#     vendas.append([produto, qtde])
#
# print(vendas)


"""
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.
"""

# nota = float(input('\n Insira uma nota entre 0 e 10: '))
# while nota < 0 or nota > 10:
#     print('\n Nota inválida!')
#     nota = float(input(' Insira uma nota entre 0 e 10: '))

"""
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.
"""

# usuario = input('\n Insira o nome de usuario: ')
# senha = input(' Senha: ')
# while senha == usuario:
#     print('\nErro! A senha deve ser diferente ao nome de usuario!')
#     usuario = input('\n Insira o nome de usuario: ')
#     senha = input(' Senha: ')

"""
3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até
o usuário inserir corretamente):

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

# nome = input(' Nome: ')
# while len(nome) <= 3:
#     print('Erro, dados invalidos!')
#     nome = input(' Nome: ')
#
# idade = int(input(' Idade: '))
# while idade < 0 or idade > 150:
#     print('Erro, dados invalidos!')
#     idade = int(input(' Idade: '))
#
# salario = float(input(' Salario (R$): '))
# while salario <= 0:
#     print('Erro, dados invalidos!')
#     salario = float(input(' Salario (R$): '))
#
# sexo = input(' Sexo ("m" ou "f": ')
# while sexo not in ('m', 'f'):
#     print('Erro, dados invalidos!')
#     sexo = input(' Sexo ("m" ou "f"): ')
#
# estadocivil = input(' Estado Civil: ')
# while estadocivil not in ('s', 'c', 'v', 'd'):
#     print('Erro, dados invalidos!')
#     estadocivil = input(' Estado Civil: ')

"""
4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.
"""

# pop_a = 80000
# tax_a = 1.03
# pop_b = 200000
# tax_b = 1.015
# anos = 0
#
# while pop_a < pop_b:
#     pop_a = pop_a * tax_a
#     pop_b = pop_b * tax_b
#     anos += 1
#
# print(f'Com as taxas de crescimento, levou-se {anos} anos para igualar as populacoes')

"""
5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.
"""

# pop_a = int(input('População do País A: '))
# while pop_a <= 0:
#     print('A população deve ser um inteiro maior que zero!')
#     pop_a = int(input('População do País A: '))
#
# tax_a = float(input('Taxa de crescimento do País A (0 - 100%): '))
# while not (1 <= tax_a <= 100):
#     print('A taxa de crescimento deve ser um numero entre 0 e 100!')
#     tax_a = float(input('Taxa de crescimento do País A (0 - 100%): '))
#
# pop_b = int(input('População do País B: '))
# while pop_b <= 0:
#     print('A população deve ser um inteiro maior que zero!')
#     pop_b = int(input('População do País B: '))
#
# tax_b = float(input('Taxa de crescimento do País B (0 - 100%): '))
# while not (1 <= tax_a <= 100):
#     print('A taxa de crescimento deve ser um numero entre 0 e 100!')
#     tax_b = float(input('Taxa de crescimento do País B (0 - 100%): '))
#
# anos = 0
#
# while pop_a < pop_b:
#     pop_a = pop_a * ((tax_a/100) + 1)
#     pop_b = pop_b * ((tax_b/100) + 1)
#     anos += 1
#
# print(f'Com as taxas de crescimento, levou-se {anos} anos para igualar as populacoes')

"""
6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o
maior faturamento
"""

# faturamentos = [0, 0, 0, 0, 0]
# i = 0
#
# while i < 5:
#     faturamentos[i] = float(input(f'Faturamento do mês {i+1}: '))
#     i += 1
# print(f'Maior faturamento: {max(faturamentos)}')

"""
7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o
faturamento total (soma) e o faturamento médio por mês (média).
"""

# fat_total = 0
# fat_mensal = 0
# for i in range(5):
#     fat_mensal = float(input(f'Faturamento do mês {i+1}: '))
#     fat_total += fat_mensal
# print(f'Faturamento total: {fat_total}')
# print(f'Faturamento médio: {fat_total/5}')

"""
8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas
a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60
(sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.
"""

# n = int(input('Insira a quantidade de pessoas da empresa: '))
#
# soma = 0
# for i in range(n):
#     idade = int(input(f'Idade da pessoa {i+1}: '))
#     soma += idade
#     i += 1
#
# print(soma)
# media = soma/n

# if 0 <= media <= 25:
#     print('A equipe é jovem!')
# elif 25 < media <= 60:
#     print('A equipe é sênior!')
# else:
#     print('A equipe é idosa!')

"""
9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.
"""

# eleitores = int(input('Insira a quantidade de eleitores: '))
# votacao = [0, 0, 0]
#
# for i in range(eleitores):
#     voto = int(input('Vote no candidato (1, 2 ou 3): '))
#     while voto not in (1, 2, 3):
#         print('Voto inválido!')
#         voto = int(input('Vote no candidato (1, 2 ou 3): '))
#     votacao[voto-1] += 1
#
# vencedor = votacao.index(max(votacao))
# print(f'Vencedor das eleições: Candidato {vencedor+1}')

"""
10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""

# qtde = int(input('Insira a quantidade de CDs: '))
# total = 0
# for i in range(qtde):
#     valor = float(input(f'Valor (R$) do CD{i+1}: '))
#     total += valor
# print(f'Total gasto (R$): {total}')
# print(f'Valor médio por CD (R$): {total/qtde}')

"""
11. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo
de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado
o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na
tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços
de 1 até 50 produtos, conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""

# print('Lojas Quase Dois - Tabela de preços')
# for i in range(50):
#     print(f'{i+1} - R$ {1.99 * (i+1):.2f}')

"""
12. Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
- Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
- Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um
programa que determine o salário desse funcionário em 2003.
"""

# aumento = 0.015
# salario = 1000 * 1.015
# for i in range(1997, 2004):
#     aumento = aumento * 2
#     salario = salario * (1 + aumento)
# print('O salário em 2003 era R$ {:.2f}'.format(salario))

"""
13. O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por
item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser
encerrado.
"""
# total = 0
# qtde = 0
#
# cardapio = [100, 1.20, 101, 1.30, 102, 1.50, 103, 1.20, 104, 1.30, 105, 1.00]
#
# codigo_pedido = int(input('Digite o código do pedido ou digite 0 para sair: '))
# while codigo_pedido != 0:
#     qtde = int(input('Quantidade: '))
#     total += cardapio[cardapio.index(codigo_pedido) + 1] * qtde
#     print(f'Total parcial: R$ {total:.2f}')
#     codigo_pedido = int(input('Digite o código do pedido ou digite 0 para sair: '))
#
# print(f'Total do pedido: R$ {total:.2f}')

"""
14. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação Python. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente
ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número
inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número
Após o final da votação, o programa deverá exibir:

a. O total de votos computados;
b. Os números e respectivos votos de todos os jogadores que receberam votos;
c. O percentual de votos de cada um destes jogadores;
d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo
número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada
jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos.
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. A disposição das infor
mações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obede
cendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador       Votos               %
9               4               50,0%
10              3               37,5%
11              1               12,5%
"""

# votos = []
# print('Enquete: Quem foi o melhor jogador?\n')
#
# for i in range(23):
#     votos.append(0)
#
# voto = int(input('Número do jogador (0 = encerrar votação): '))
# while voto != 0:
#     votos[voto - 1] += 1
#     voto = int(input('Número do jogador (0 = encerrar votação): '))
#
# print('\nResultado da votação:')
# print(f'Foram computados {sum(votos)} votos.')
# print('\nJogador\tVotos\t%')
# for i in range(23):
#     print(f'#{i+1}\t{votos[i]}\t{votos[i]/sum(votos):.2%}')
#
# print(f'\nMelhor jogador da partida: #{votos.index(max(votos)) +1}')
# print(f'Total de votos: {votos[votos.index(max(votos))]} votos.')
# print(f'% de votos: {votos[votos.index(max(votos))] / sum(votos):.2%}')
