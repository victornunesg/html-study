# ----------------------------
# TUPLES
# ----------------------------
# Tuples - faster Lists you can't change
# They are faster to work with than regular lists, but are not flexible as lists
# Protect the database due it's immutable
# Mostly used to heterogeneous data
# The only code difference is: use () instead of []
# Can be used without () but is totally not recommended

friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
print(friends)
print(friends_tuple)

# We can access the elements in the same way, also slice
# But we can't use append/insert or change data because tuples are immutable, just the functions to get data from it
# Tuples are declared using () but to get data from an index we should use [], as lists
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

# Acessando valores da tupla - unpacking
# UNPACKING - Desmembrar a tupla em várias variáveis, de uma só vez (ao inves de identificar o indice de cada info)
# é necessário respeitar a quantidade de valores da tupla (5) e variáveis (5)
nome, data_contratacao, data_nascimento, salario, cargo = vendas
print(salario)
print(data_nascimento)

# o unpacking também pode ser usado em listas, o problema é que a lista pode ser aumentada em valores
# o comando enumerate que usamos em listas, na realidade cria uma tupla



# ----------------------------
# SETS
# ----------------------------
# Sets - blazingly fast unordered Lists
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric', 'Eric'}

print(friends)
print(friends_tuple)
print(friends_set)

# Main difference, set is unordered and removes duplicated values
# It is way faster to search in it than regular lists

my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}
print(friends_set.intersection(my_friends_set))  # gives the indexes in common between two sets
print(friends_set.difference(my_friends_set))  # gives the indexes different between two sets
print(friends_set.union(my_friends_set))  # all names in both sets with no duplicates

# ----------------------------
# EMPTY TYPES OF LIST CREATION
# ----------------------------
# Creating empty types of lists:
# empty Lists
empty_list = []
empty_list = list()

# empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# empty Set
empty_set = {}  # this is wrong, this is a dictionary
empty_set = set()
