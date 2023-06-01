print('\n===========================================================')
print('FUNÇÕES')
print('===========================================================')
"""
As functions são blocos de código que servem 1 único propósito, fazem uma ação específica.
Sempre declare uma função antes de usá-la
Após a declaração, todas as linhas identadas serão parte da função

ESTRUTURA BÁSICA:
def nome_funcao():
    faça alguma coisa
    faça outra coisa
    return valor_final

Exemplo: vamos criar uma função de cadastro de um Produto.
Essa função deve garantir que o produto cadastrado está em letra minúscula."""


# def cadastrar_produto():
#     produto = input('Digite o nome do produto que deseja cadastrar: ')
#     produto = produto.casefold()  # método que coloca as letras em minúsculo (ou lower() serve tb)
#     produto = produto.strip()  # método que remove espaços em branco na string
#     return produto  # a partir dessa linha, a função não executa mais nada.
#     # É o retorno/resposta da função, podemos armazenar em uma variável, conforme a seguir.
#     # essa variável produto só existe dentro da função, diferentemente das variáveis do código
#
#
# # usando a função para armazenar seu retorno em uma variável:
# variavel_produto = cadastrar_produto()
# print(variavel_produto)

print('\n===========================================================')
print('ARGUMENTOS/PARÂMETROS DA FUNÇÃO')
print('===========================================================')

"""
ESTRUTURA:
def minha_funcao(parametro1, parametro2, parametro3):
    return parametro1 + parametro2 + parametro3
"""


# def minha_soma(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# # chamando a função com os argumentos
# soma = minha_soma(10, 20, 0)
# print(soma)

"""
EXEMPLO PRÁTICO:
Vamos criar uma function com parâmetro
Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.
Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.

Ex:
Vinho -> BEB12302
Cerveja -> BEB12043
Vodka -> BEB34501

Guaraná -> BSA11104
Coca -> BSA54301
Sprite -> BSA34012
Água -> BSA09871

Repare que bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.
Crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais produtos
devem ser enviados para a área de bebidas alcóolicas."""

# produtos = ['beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448',
#             'CAR23596', 'CAR13490', 'BEB21365', 'BEB31623', 'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694',
#             'BSA11769', 'BEB19495', 'TFA14792', 'TFA78043', 'BSA33484', 'BEB97471', 'BEB62362', 'TFA27311',
#             'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947', 'TFA58799', 'CAR94811',
#             'BSA59251', 'BEB15385', 'BEB24213', 'BEB56262', 'BSA96915', 'CAR53454', 'BEB75073']
#
#
# def analise_produto(lista_produtos):
#     print('Bebidas alcóolicas, conduzir à área correspondente:')
#     for item in lista_produtos:
#         if 'BEB' in item.upper():
#             print(f'Item: {item}')
#
#
# analise_produto(produtos)
#
# # Outra forma de fazer:
#
#
# def ehalcoolico(bebida):
#     bebida = bebida.upper()
#     if 'BEB' in bebida:
#         return True
#     else:
#         return False
#
#
# for produto in produtos:
#     if ehalcoolico(produto):
#         print('Enviar {} para setor de bebidas alcóolicas'.format(produto))

""" Mais de 1 argumento e formas de passar argumento para uma função

ESTRUTURA:
Existem 2 formas de passar o argumento:
- Em ordem (positional argument)
- Com o nome do argumento (keyword argument)

EXEMPLO:
Alterando a função anterior para conseguir categorizar qualquer tipo de bebida de acordo com o "rótulo" passado para
a função. Agora temos que verificar se o produto é da categoria passada ou não.
"""


# def eh_da_categoria(bebida, categoria):
#     bebida = bebida.upper()
#     if categoria in bebida:
#         return True
#     else:
#         return False
#
#
# for produto in produtos:
#     if eh_da_categoria(categoria='BEB', bebida=produto):  # Com o nome do argumento (keyword argument)
#         print('Enviar {} para setor de bebidas alcóolicas'.format(produto))
#     elif eh_da_categoria(produto, 'BSA'):  # Em ordem (positional argument)
#         print('Enviar {} para setor de bebidas não alcóolicas'.format(produto))

"""
Outro exemplo, a função print tem um parâmetro que define qual caracter será utilizado entre a impressão das entradas,
chamado 'sep', que deve ser declarado sempre ao final, pois é um parâmetro de palavra chave e não de posição, conforme
ilustrado a seguir """

# qtde_produtos = len(produtos)
# print('Quantidade total de produtos:', qtde_produtos, 'texto2',  'texto3', sep='\n')





# def greeting(name1):
#     print(f'Hello {name1}!')
#
#
# greeting('Brian')  # calling a function
#
# # Using a function with multiple parameters
#
#
# def greeting(name2, age2):
#     print(f'Hello {name2}, you are {age2} years old!')
#
#
# greeting('Brian', '29')  # calling a function
#
# # Using a function with default parameter value
#
#
# def greeting(name3, age3='28'):
#     print(f'Hello {name3}, you are {age3} years old!')
#
#
# greeting('Judith')  # calling a function
#
# # Using a function with variable obtained by an input from user
#
#
# def greeting(name4, age4):
#     print(f'Hello {name4}, you are {age4} years old!')
#
#
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greeting(name, age)  # calling a function
#
# # ----------------------------
# # EXERCISE
# # ----------------------------
# print('')
# print('EXERCISE')
# print('')
# '''
# def greeting(name, age=28):
#     #Greets user with 'name' from 'input box' and 'age', if available, default age is used
#     print('Hello '  +  name + ', you are ' + str(age) +'!')
#     print(f'Hello {name}, you are {age} years old!')
#
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# greeting(name, age)
# # 1. Add new print statement - on a new line
# #    which says 'We hear you like the color xxx! xxx is a string with color
# # 2. extend the function with another  input parameter 'color', that defaults to 'red'
# # 3. Capture the color via an input box as variable:color
# # 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
# #  adding 1 to the age
# # 5. Capitalize first letter of the 'name', and rest are small caps
# # 6. Favorite color should be in lowercase
# '''
#
#
# def greeting(name5, age5=28, color1='red'):
#     # Greets user with 'name' from 'input box', 'color' 'age'. If unavailable, default age and color are used
#     print('')
#     print(f'Hello {name5.capitalize()}, you will be {age5+1} years old next birthday!')
#     print(f'We hear you like the color {color1.lower()}!')
#
#
# name5 = input('Enter your name: ')
# age5 = input('Enter your age: ')
# color1 = input('Enter a color you like: ')
# print('')
# greeting(name5, int(age5), color1)
#
# # Named notation: it's best to name the arguments when calling the function to let the program more readable
# # and also to be possible to change the order of the arguments
# print('')
# greeting(age5=29, color1='gray', name5='Victor Gomes')
#
# # ----------------------------
# # RETURN STATEMENTS
# # ----------------------------
#
# # Sometimes we want a function to give us a data back, in return
#
#
# def value_added_tax(amount):
#     tax = amount * 0.25
#
#
# print('')
# print(value_added_tax(100))  # in this case it will return 'none'
#
# # Modifying the function to return a data
#
#
# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return amount, tax, total_amount  # when we have more than 1 item returned, Phyton return us a tuple
# # return [amount, tax, total_amount]  # now a list will be outputted
# # return {amount, tax, total_amount}  # now a set will be outputted
# # return f'{amount}, {tax}, {total_amount}'  # now a string will be returned
#
#
# print('')
# price = value_added_tax(100)
# print(price)  # a list will be returned
# # print(price[1])  in this case only the tax will be returned
