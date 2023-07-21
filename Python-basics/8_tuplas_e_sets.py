print('\n===========================================================')
print('TUPLAS')
print('===========================================================')
""" Tuplas - listas rápidas, imutáveis
São mais rápidas de se trabalhar do que lists, porém não são flexíveis como elas
Protegem os dados tendo em vista que são imutáveis
Mais utilizada com dados heterogêneos
No código, a única distinção se dá pelo uso de () ao invés de []
Pode ser utilizada/declarada sem os () porém é totalmente não recomendado """

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
print(friends)
print(friends_tuple)

# Podemos acessar os itens do mesmo jeito das listas, até o slice, entretanto não podemos usar append/insert ou alterar
# dados pois tuplas são imutáveis. Usamos apenas funções para coletar os valores delas.
# Tuplas são declardadas com () porém utilizamos [] para coletar dados de um index, do mesmo jeito das listas
print(friends[2:4])
print(friends_tuple[2:4])

# Tupla com dados heterogêneos
vendas = ('Lira', '25/08/2020', '15/02/1994', 1000, 'Estagiário')
print(vendas)

# Acessando valores da tupla - modo convencional
nome = vendas[0]
data_contratacao = vendas[1]
data_nascimento = vendas[2]
salario = vendas[3]
cargo = vendas[4]

print('\n===========================================================')
print('ACESSANDO VALORES DAS TUPLAS - UNPACKING')
print('===========================================================')
# UNPACKING - Desmembrar a tupla em várias variáveis, de uma só vez (ao inves de identificar o indice de cada info)
# é necessário respeitar a quantidade de valores da tupla (5) e variáveis (5)
nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(salario)
print(data_nascimento)

# o unpacking também pode ser usado em listas, o problema é que a lista pode ser aumentada em valores
# o comando enumerate que usamos em listas, na realidade cria uma tupla

print('\n===========================================================')
print('SETS')
print('===========================================================')
"""
SETS - diferenciam-se por não conter valores duplicados e não serem ordenados
Utilizamos {} na declaração de um set
Sets são bem mais rápidos em mecanismo de buscas do que listas regulares

Caso de uso: quando queremos remover duplicados de uma lista, basta transformar em set e depois em lista novamente.

Exemplo: Quantos clientes tivemos na loja?
"""
cpf_clientes = ['762.196.080-97', '263.027.380-67', '827.363.930-40', '925.413.640-91', '870.565.160-33',
                '892.080.930-50', '462.126.030-81', '393.462.330-10', '393.462.330-10', '393.462.330-10',
                '988.305.810-11', '596.125.830-05', '596.125.830-05', '990.236.770-48']

print(f'Temos {len(cpf_clientes)} registros de cpf em "cpf_clientes" ')
set_cpf_clientes = set(cpf_clientes)  # transformando a lista em um set
cpf_clientes_unicos = list(set_cpf_clientes)  # transformando o set em uma nova lista
print('Tivemos {} clientes na loja'.format(len(set_cpf_clientes)))

print('\n===========================================================')
print('MÉTODOS DE SETS')
print('===========================================================')

# add -> adiciona um item no set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.add('airpod')
print(meu_set)

# remove -> retira um item de um set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.remove('iphone')
print(meu_set)

# clear -> retira todos os itens de um set
meu_set = {'iphone', 'macbook', 'ipad'}
meu_set.clear()
print(meu_set)

# union -> junta as informações de 2 sets. Se houver algum valor duplicado, ele constará apenas 1 vez no set final
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
todos_produtos = produtos.union(lancamentos)
print(todos_produtos)

# intersection -> pega apenas as informações que existem nos 2 sets ao mesmo tempo
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
intersecao = produtos.intersection(lancamentos)
print(intersecao)

# difference -> retorna todas as informações de um set que não fazem parte de outro set
produtos = {'iphone', 'macbook', 'ipad'}
lancamentos = {'airpod', 'apple watch', 'ipod', 'ipad'}
produtos_nao_lancamentos = produtos.difference(lancamentos)
print(produtos_nao_lancamentos)  # repare que ipad foi retirado do resultado porque ele estava contido no set de
# lançamentos

print('\n===========================================================')
print('CRIAÇÃO DE LISTAS/TUPLAS/SETS VAZIOS')
print('===========================================================')

# Listas vazias
empty_list = []
empty_list = list()
print(empty_list)

# Tuplas vazias
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)

# Sets vazios
empty_set = {}  # jeito errado, desta forma estaremos criando um dicionário
empty_set = set()
print(empty_set)
