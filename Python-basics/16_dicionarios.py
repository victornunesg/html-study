print('\n===========================================================')
print('DICIONÁRIOS')
print('===========================================================')

"""
Dicionários armazenam pares de 'chave:valor'. Você busca pela chave/palavra e recebe o valor referente a ela.
É como se fosse uma tabela de banco de dados, chave -> valor
É possível obter uma informação através de uma chave ao invés de index (não recomendado pegar pelo index).
Não deve ser usado para pegar itens em uma determinada ordem
Podem ter valores heterogêneos (vários tipos de valores em um mesmo dicionário)
As chaves são únicas, obrigatoriamente. Caso haja a mesma chave para dois valores diferentes, um será ignorado.
"""

print('\n===========================================================')
print('CRIAR UM DICIONÁRIO')
print('===========================================================')


# Definindo um dicionário vazio
movie = {}
print(movie)

# Definindo um dicionário com valores
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']
}
print(movie)

detail = {
    'time': '110 minutes',
    'location': 'Miami',
}
print(detail)

print('\n===========================================================')
print('COLETANDO ITENS DO DICIONÁRIO')
print('===========================================================')


# Imprimindo o dicionário por completo
print(movie)

# Imprime somente um item, através da chave
print(movie['title'])

# Método GET é o mais indicado para printar itens, pois utilizando o comando acima, caso a chave não exista, o programa
# apresentará um erro durante a compilação. O método GET retona um objeto vazio 'none', não dá erro.
# Adicionalmente, em versões anteriores do Python a ordem do dicionário poderia sofrer alterações em tempo de compilação
print(movie.get('title'))
print(movie.get('budget'))  # retorna objeto vazio, 'none'
print(movie.get('budget', 'not found'))  # é possível setar um valor padrão para objetos vazios
print(movie)
print('')

# Verificando se existe um item no dicionário - Opção 1
if 'credit' in movie:  # Neste caso estamos procurando 'credit' nas chaves do dicionário
    print(movie['credit'])
else:
    print('Credit does not exist in Movie')

# Verificando se existe um item no dicionário - Opção 2
if movie.get('credit') is None:  # Utilizando o método GET
    print('Credit does not exist in Movie')
else:
    print(movie['credit'])

print('\n===========================================================')
print('ADICIONAR, MOVER E MODIFICAR ITENS DO DICIONÁRIO')
print('===========================================================')

# Adicionando um novo item ao dicionário
movie['budget'] = 2500

# Modificando itens existentes separadamente
movie['title'] = 'The Holy Grail'

# Modificando o dicionário por inteiro usando o método update ()
movie.update({'title': 'Fast and Furious', 'year': 2002, 'cast': ['Paul Walker', 'Vin Diesel', 'Tyrese Gibson']})
print(movie)

# Também é possível adicionar um dicionário a outro (com chaves distintas):
movie.update(detail)
print(movie)

print('\n===========================================================')
print('DELETANDO ITENS DO DICIONÁRIO')
print('===========================================================')

# Deletando itens separadamente
del movie['year']  # deleting individually

# Usando o método pop, é análogo a listas, tira o item e pode armazenar em uma outra variável caso queira usar
movie.pop('budget')
time = movie.pop('time')
print(movie)
print(time)
print('')

# Deleta os itens do dicionário, esvaziando/limpando o dicionario (mas a variável ainda existirá)
movie.clear()
print(movie)

# Deleta o dicionário por completo, a variável não existe mais
del detail

print('\n===========================================================')
print('LOOP FOR EM DICIONÁRIO')
print('===========================================================')

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# Demonstrando o FOR
for chave in vendas_tecnologia:
    print('{}: {} unidades'.format(chave, vendas_tecnologia[chave]))

# Qual o total de notebooks vendidos?
total_notebooks = 0
for chave in vendas_tecnologia:
    if 'notebook' in chave:
        total_notebooks += vendas_tecnologia[chave]
print(total_notebooks)

# Imprime o par chave e valor através do método items
for chave, valor in vendas_tecnologia.items():
    print(chave, valor)

print('\n===========================================================')
print('MEMBERSHIP')
print('===========================================================')

# Dicionários não são ordenados e não podem conter valores duplicados (pelo menos nas chaves)
print('')
python = {'John': 35, 'Eric': 36, 'Michael': 35, 'Terry': 38, 'Graham': 37, 'TerryG': 34}
holy_grail = {'Arthur': 40, 'Galahad': 35, 'Lancelot': 39, 'Knight of NI': 40, 'Zoot': 17}
life_of_brian = {'Brian': 33, 'Reg': 35, 'Stan/Loretta': 32, 'Biccus Diccus': 45}

# Verifica se há uma chave no dicionário
print('Arthur' in holy_grail)
if 'Arthur' not in python:
    print('He\'s not here')

# Juntando dicionários
people = {}
people1 = {}
people2 = {}

# Método 1 - UPDATE
people.update(python)  # copying python dictionary into people
print(people)
people.update(holy_grail)  # already have python dictionary, adding holy grail
print(people)
people.update(life_of_brian)  # already have python dictionary, adding holy grail
print(people)
print('')

# Método 2 - LOOP FOR (COMPREHENSION)
for groups in (python, holy_grail, life_of_brian):
    people1.update(groups)
print(people1)
print('')

# Método 3 - UNPACKING
people2 = {**python, **holy_grail, **life_of_brian}
print(people2)
print('')

# Ordenando itens
print(sorted(people.items()))
print(sorted(people1.items()))
print(sorted(people2.items()))

# Calculando a soma dos valores (caso haja valores diferentes de números, irá dar erro)
print('\nThe sum of the ages: ', sum(people.values()))


print('\n===========================================================')
print('MÉTODOS ITEMS() / KEYS() / VALUES()')
print('===========================================================')

# Cada um desses métodos transforma o dicionário em tuplas ou listas. Entretanto, não conseguimos executar os métodos
# padrão de cada um dos tipos, pois é como se criássemos uma cópia vinculada ao dicionário (dict_items)
# Para desvincular do dicionário, usamos o método TUPLE() ou LIST() dependendo do cenário, para transformar efetivamente
# em uma tupla/lista separada para facilitar a manipulação/ordenação.
# O FOR funciona normalmente nos dict_items / dict_keys / dict_values

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000,
                     'notebook asus': 2450}

# items() - Retorna uma lista em que cada item é uma tupla com (chave, valor)
dict_itens = vendas_tecnologia.items()
print(dict_itens)
# Por ser um 'dict_item' e estar vinculada ao dicionário a variável atualiza automaticamente após a adição/deleção de
# itens no dicionário:
vendas_tecnologia['liraphone'] = 1000
print(dict_itens)
# Para desvincular do dicionário, usamos o método TUPLE() para transformar efetivamente em uma lista separada
print(vendas_tecnologia)
print(tuple(dict_itens))
tupla_itens = tuple(dict_itens)
vendas_tecnologia['victorphone'] = 50000
print(tupla_itens)
print('')

# values() - Retorna uma lista com todos os valores do dicionários
dict_valores = vendas_tecnologia.values()
print(dict_valores)
lista_valores = list(dict_valores)
print(lista_valores)
print('')

# keys() - Retorna uma lista com todas as chaves do dicionário
dict_chaves = vendas_tecnologia.keys()
print(dict_chaves)
lista_chaves = list(dict_chaves)
print(lista_chaves)
print('')

# Exemplo - Ordene em ordem alfabética as vendas de tecnologia, por produto (com dict_keys não é possível):
lista_chaves.sort()
for chave in lista_chaves:
    print(f'{chave}: {vendas_tecnologia[chave]} unidades.')

print('\n===========================================================')
print('TRANSFORMANDO LISTAS EM DICIONÁRIOS E FUNÇÃO .ZIP()')
print('===========================================================')

""" Estrutura:
Dicionário com valores padrões:
    dicionario = dict.fromkeys(lista_chaves, valor_padrao)

Dicionário a partir de listas de tuplas:
    dicionario = dict(lista_tuplas)

Dicionário a partir de 2 listas:
    Passo 1: Transformar listas em lista de tuplas com o método zip
    Passo 2: Transformar em dicionario

    lista_tuplas = zip(lista1, lista2)
    dicionario = dict(lista_tuplas)
"""

produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

lista_tuplas = zip(produtos, vendas)  # criando lista de tuplas com ZIP - nesse caso transforma em um zip object
print(lista_tuplas)  # zip object
dicionario_vendas = dict(lista_tuplas)  # com o zip object é possível criar um dicionário
print(dicionario_vendas)  # dicionário pronto

# QUANTO VENDEMOS DE IPAD?
# Fazendo através de listas
indice = produtos.index('ipad')
print(f'Vendemos {vendas[indice]} unidades de iPad.')

# Fazendo através de dicionário
print(f'Vendemos {dicionario_vendas["ipad"]} unidades de iPad.')

# =================================
# CARTILHA DE MÉTODOS ESPECÍFICOS DE DICIONÁRIO
# =================================

"""
- len() -> retorna o tamanho do dicionário, quantas entradas existem
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(len(vendas_mes))

- clear() -> Deleta todos os elementos do Dicionário (semelhante ao que aprendemos em listas)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_mes.clear()
print(vendas_mes)

- copy() -> Cria uma cópia do dicionário (semelhante ao que aprendemos em listas)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas2_mes = vendas_mes.copy()
print(vendas2_mes)

- fromkeys(chaves, valor_padrao) -> Cria um dicionário com as chaves e o mesmo valor padrão para todas as chaves
chaves = ('jan', 'fev', 'mar')
vendas = 100
vendas_mes = dict.fromkeys(chaves, vendas)
print(vendas_mes)

- get(chave) -> 	Retorna o valor especificado pela chave (Semelhante a fazer dictionario[chave])
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(vendas_mes.get('mar'))

- keys() -> Retorna uma lista com todas as chaves do dicionário
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.keys()))

- values() -> Retorna uma lista com todos os valores do dicionários
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.values()))

- items() -> Retorna uma lista em que cada item é uma tupla com (chave, valor)
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
print(list(vendas_mes.items()))

- pop(chave) -> Retira o item do dicionário e retorna o valor dele para ser usado
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.pop('fev') #retira o fevereiro do dicionário ao mesmo tempo que armazena o valor dele na variável
print(vendas_mes)
print(vendas_fev)

- popitem() -> Retira o último item adicionado ao dicionário
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
#retira o último item adicionado no dicionário ao mesmo tempo que armazena o item(chave, valor) dele na variável
vendas_ult = vendas_mes.popitem() 
print(vendas_mes)
print(vendas_ult)

- setdefault(chave, valor) -> Retorna o valor da chave passada, mas caso a chave não exista, cria no dicionário o item com a chave e valor passados.
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_fev = vendas_mes.setdefault('fev', 500)
print(vendas_fev)
#repare que como fevereiro existe na lista, ele procura pelo valor de fevereiro e ignora o 500 passado
#agora quando não existe na lista:
vendas_abr = vendas_mes.setdefault('abr', 600)
#repare que agora além de vendas_abr retornar o 600 como valor, ele adicionou um item no dicionario
print(vendas_abr)
print(vendas_mes)

- update(dicionario) -> Adiciona o dicionário passado como parâmetro ao dicionário original
vendas_mes = {'jan': 150, 'fev': 100, 'mar': 190}
vendas_2tri = {'abr': 400, 'mai': 600, 'jun': 500}
vendas_mes.update(vendas_2tri)
print(vendas_mes)
"""


