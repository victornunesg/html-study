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

2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
uma mensagem de erro e voltando a pedir as informações.

3. Faça um programa que leia e valide as seguintes informações (e para cada uma delas, continue pedindo a informação até
o usuário inserir corretamente):

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que
a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas
de crescimento.

5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
entrada e permita repetir a operação.

6. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o
maior faturamento

7. Faça um programa que peça para o usuário inserir o faturamento dos últimos 5 meses (individualmente) e informe o
faturamento total (soma) e o faturamento médio por mês (média).

8. Faça um programa que consiga categorizar a idade das equipes de uma empresa. Faça um programa que peça para n pessoas
a sua idade, ao final o programa devera verificar se a média de idade da equipe varia entre 0 e 25 (jovem) ,26 e 60
(sênior) e maior que 60 (idosa); e então, dizer se a equipe é jovem, sênior ou idosa, conforme a média calculada.

9. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
votar e ao final mostrar o número de votos de cada candidato.

10. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

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