print('\n===========================================================')
print('SPLIT')
print('===========================================================')

msg = 'Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

# split transforma uma string em uma lista
print(list(msg))  # o 'cast' cria uma lista a partir da string, porém quebrando em caracteres separadamente
print(msg.split())  # usando split, transformamos a string em uma lista, mas separada por palavras
print(msg.split(':'))  # é possível passar como parâmetro onde se deseja realizar a quebra da string

print('\n===========================================================')
print('JOIN')
print('===========================================================')
# join faz o oposto, transforma uma lista em uma string
print(str(friends_list))  # o 'cast' não traz o resultado esperado, pois ainda se assemelha a uma lista
print(','.join(friends_list))  # criando uma string a partir da lista, utilizando a vírgula como separador
print('-'.join(friends_list))  # utilizando agora o hífen como separador

print('')

# podemos realizar múltiplas operações usando split e join, também podemos usar o replace como alternativa
print(''.join(msg.split()))
print(msg.replace(' ', ''))  # exemplo, usando o replace para remover espaços em branco em uma string

print('\n===========================================================')
print('EXERCÍCIO')
print('===========================================================')

# A partir da string 'csv', preencha a lista 'friends_list' com os nomes de todos os amigos, 1 por posição

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

print(csv)
print(csv.split(';'))
print(','.join(csv.split(';')))
print(','.join(csv.split(';')).split(':'))
print(','.join(','.join(csv.split(';')).split(':')))
print((','.join(','.join(csv.split(';')).split(':'))).split(','))
print(' ')
friends_list = ((csv.replace(':', ',').replace(';', ',')).split(','))
print(friends_list)
