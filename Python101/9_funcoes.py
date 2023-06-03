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

produtos = ['beb46275', 'TFA23962', 'TFA64715', 'TFA69555', 'TFA56743', 'BSA45510', 'TFA44968', 'CAR75448',
            'CAR23596', 'CAR13490', 'BEB21365', 'BEB31623', 'BSA62419', 'BEB73344', 'TFA20079', 'BEB80694',
            'BSA11769', 'BEB19495', 'TFA14792', 'TFA78043', 'BSA33484', 'BEB97471', 'BEB62362', 'TFA27311',
            'TFA17715', 'BEB85146', 'BEB48898', 'BEB79496', 'CAR38417', 'TFA19947', 'TFA58799', 'CAR94811',
            'BSA59251', 'BEB15385', 'BEB24213', 'BEB56262', 'BSA96915', 'CAR53454', 'BEB75073']


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

print('\n===========================================================')
print('VALORES PADRÃO PARA OS ARGUMENTOS DA FUNÇÃO')
print('===========================================================')

""" ESTRUTURA: 
def minha_funcao(argumento = valor_padrao):
    ...
    return ..  

Vamos criar uma função que padronize códigos de produtos. O default será padronizar os códigos para letras minúsculas
(dado por 'm'), mas se o usuário quiser pode padronizar para maiúscula, dado por ('M').
"""


# def padronizar_codigos(lista_codigos, padrao='m'):
#     for i, item in enumerate(lista_codigos):
#         item = item.replace('  ', ' ')
#         item = item.strip()
#         if padrao == 'm':
#             item = item.lower()
#         elif padrao == 'M':
#             item = item.upper()
#         lista_codigos[i] = item
#     return lista_codigos
#
#
# cod_produtos = [' ABC12 ', 'abc34', 'AbC37']
# print(padronizar_codigos(cod_produtos))
# print(padronizar_codigos(cod_produtos, 'M'))

print('\n===========================================================')
print('MAIS SOBRE O RETURN')
print('===========================================================')

"""
Podemos usar o return para basicamente qualquer tipo de objeto: numero, string, lista, tupla, dicionario, etc
O return, se for executado, encerra a função, mesmo que dentro dela haja um loop
"""


# # retornar um número
# def minha_soma(num1, num2, num3):
#     return num1 + num2 + num3
#
#
# # retornar um texto
# def padronizar_texto(texto):
#     texto = texto.casefold()
#     texto = texto.replace("  ", " ")
#     texto = texto.strip()
#     return texto
#
#
# # retornar um boolean
# def bateu_meta(vendas, meta):
#     if vendas >= meta:
#         return True
#     else:
#         return False
#
#
# # retornar uma lista, tupla ou dicionario
# def filtrar_lista_texto(lista, pedaco_texto):
#     lista_filtrada = []
#     for item in lista:
#         if pedaco_texto in item:
#             lista_filtrada.append(item)
#     return lista_filtrada
#
#
# # retornar mais de um objeto
# # funções retornam, por padrão, uma tupla automaticamente quando há mais de um valor no return
# def operacoes_basicas(num1, num2):
#     soma = num1 + num2
#     diferenca = num1 - num2
#     mult = num1 * num2
#     divisao = num1 / num2
#     return soma, diferenca, mult, divisao
#
#
# print(operacoes_basicas(10, 2))


# def value_added_tax(amount):
#     tax = amount * 0.25
#     total_amount = amount * 1.25
#     return amount, tax, total_amount  # quando temos mais de um parametro, por padrão, o Python retorna uma Tupla
# # return [amount, tax, total_amount]  # agora uma lista será retornada
# # return {amount, tax, total_amount}  # agora um set será retornado
# # return f'{amount}, {tax}, {total_amount}'  # agora uma string será retornada

print('\n===========================================================')
print('DOCSTRING E ANNOTATIONS')
print('===========================================================')

"""
São ferramentas "apenas" para organização:
Quando criamos uma função, normalmente não seremos as únicas pessoas a usarem essa função e também pode ser que a gente
precise usar essa mesma função semanas, meses ou até anos depois da sua criação.

Por isso é importante usarmos DocStrings e Annotations

Docstring -> diz o que a função faz, quais valores ela tem como argumento e o que significa cada valor
Annotation -> diz o que devem ser os argumentos e o que a função retorna

Em muitas empresas, o time de tecnologia vai ter um padrão que você deve seguir para isso, mas caso não tenha, vamos te
mostrar um padrão bom a ser utilizado.
"""


# # DOCSTRING
# def minha_soma(num1, num2, num3):
#     """Faz a soma de 3 números inteiros e devolve como resposta um inteiro
#
#     Parameters:
#         num1 (int): primeiro número a ser somado
#         num2 (int): segundo número a ser somado
#         num3 (int): terceiro número a ser somado
#
#     Returns:
#         soma (int): o valor da soma dos 3 números dados como argumento
#     """
#     return num1 + num2 + num3
#
#
# # ANNOTATION
# def minha_soma(num1: 'primeiro número a ser somado', num2: int, num3: int) -> int:
#     return num1 + num2 + num3


print('\n===========================================================')
print('EXCEÇÕES E ERROS EM FUNÇÕES')
print('===========================================================')

""" Sempre que usamos o try para testar uma condição, o except é obrigatório
ESTRUTURA:
try:
    o que eu quero tentar fazer
except:
    raise Exception (o que vou fazer caso dê erro)
    
ou então avisando qual o tipo de erro que ele teve:

raise TypeError('O erro foi esse')
raise ValueError('O erro foi esse')
raise ZeroDivisionError('O erro foi esse')

Ponto de atenção: o try tenta executar todas as linhas do bloco identado, então pode ser que o erro esteja em uma linha
que não seja a que estamos querendo analisar, daí a mensagem do except vai estar incoerente com o erro

TRATAMENTO COMPLETO
try:
    tente fazer isso
except ErroEspecífico:
    deu esse erro aqui que era esperado 
else:
    caso não dê o erro esperado, rode isso.
finally:
    independente do que acontecer, faça isso.
"""


# def descobrir_servidor(email):
#     try:
#         posicao_a = email.index('@')
#     except:
#         # usamos o raise para interromper o programa
#         raise ValueError('Email digitado não tem @, digite novamente')
#     else:
#         servidor = email[posicao_a:]
#         if 'gmail' in servidor:
#             return 'gmail'
#         elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
#             return 'hotmail'
#         elif 'yahoo' in servidor:
#             return 'yahoo'
#         elif 'uol' in servidor or 'bol' in servidor:
#             return 'uol'
#         else:
#             return 'não determinado'
#
#
# email = input('Digite o seu e-mail: ')
# print(descobrir_servidor(email))

print('\n===========================================================')
print('QUANTIDADE INDEFINIDA DE ARGUMENTOS')
print('===========================================================')
""" Utilidade:

Quando você quer permitir uma quantidade indefinida de argumentos, usa o * para isso.

Estrutura:

*args para positional arguments -> argumentos vêm em formato de tupla

def minha_funcao(*args):
    ...

**kwargs para keyword arguments -> argumentos vêm em formato de dicionário

def minha_funcao(**kwargs):
    ... 
"""


# # POSITIONAL ARGUMENTS
# def minha_soma(*numeros):
#     print(numeros)
#     soma = 0
#     for numero in numeros:
#         soma += numero
#     return soma
#
#
# print(minha_soma(10, 13, 1, 10, 90, 0, 9, 8))  # a saída será uma tupla
#
#
# # KEY ARGUMENTS
# def preco_final(preco, **adicionais):
#     print(adicionais)
#     if 'desconto' in adicionais:
#         preco *= (1 - adicionais['desconto'])
#     if 'garantia_extra' in adicionais:
#         preco += adicionais['garantia_extra']
#     if 'imposto' in adicionais:
#         preco *= (1 + adicionais['imposto'])
#     return preco
#
#
# print(preco_final(1000, desconto=0.1, garantia_extra = 100, imposto=0.3))  # a saída será um dicionário

print('\n===========================================================')
print('ORDEM DOS ARGUMENTOS')
print('===========================================================')

""" Estrutura:

Sempre os positional arguments vêm antes e depois os keywords arguments.
Sempre os argumentos individuais vêm antes e depois os "múltiplos"

def minha_funcao(arg1, arg2, arg3, arg4, *args, k = kwarg1, k2 = kwarg2, k3 = kwarg3, **kwargs):
    ...

Caso coloquemos argumentos múltiplos antes dos individuais, o Python não vai saber quando começam os individuais, com
isso o código dá erro.
"""