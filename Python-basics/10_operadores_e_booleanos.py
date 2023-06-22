print('\n===========================================================')
print('OPERADORES')
print('===========================================================')

a = 7  # operador de atribuição, atribuindo valor a uma variável
b = 3

print('a = ', a)
print('b = ', b)
print('a == b is', a == b)  # verificando se 'a' é igual a 'b'
print('a != b is', a != b)  # verificando se 'a' é diferente de 'b'
print('a > b is', a > b)  # verificando se 'a' é maior que 'b'
print('a < b is', a < b)  # verificando se 'a' é menor que 'b'
print('a >= b is', a >= b)  # verificando se 'a' é maior que ou igual a 'b'
print('a <= b is', a <= b)  # verificando se 'a' é menor que ou igual a 'b'

# operador 'in' verifica pertença
print('')
print('o in John is ', 'o' in 'John')  # checking if 'o' is found the string 'John'
print('o in John is ', 'o' not in 'John')  # checking if 'o' is not found the string 'John'
print('John is John is ', 'John' is 'John')  # identity
print('John is not John is ', 'John' is not 'John')  # negative identity

# operador de identidade, verifica se duas coisas são idênticas
print('')
a = [3, 7, 42]
b = [3, 7, 42]
print(a == b)  # retorna True porque 'a' se parece com 'b', eles são iguais (em valor)
print(a is b)  # retorna False porque 'a' não ocupa o mesmo espaço de memória de 'b', eles não são idênticos
print(id(a), id(b))  # mostra a posição de memória de cada um

print('\n===========================================================')
print('BOOLEANOS')
print('===========================================================')

print(int(True))  # tornando 'True' booleano em inteiro retorna 1
print(int(False))  # tornando 'False' booleano em inteiro retorna 0
print(bool('Parrot'))  # transformando uma string em boolean retorna 'True'
print(bool(' '))  # transformar uma string com um espaço em booleano também retorna 'True'
print(bool(1))  # transformando objetos diferentes de zero em booleanos retorna 'True':
print(bool(50.2))  # float
print(bool([1, 2]))  # listas

# Objetos vazios e zeros retornam 'False' quando transformados em booleano
print(bool(''))
print(bool(0))
print(bool([]))

# Valores triviais são avaliados como 0
# Valores não triviais para 1

# Valores 'booleanos' podem ser convertidos para números
print(42 + True)  # retorna 42 + 1 = 43
print(42 + False)  # retorna 42 + 0 = 42
