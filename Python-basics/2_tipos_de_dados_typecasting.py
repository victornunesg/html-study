print('\n===========================================================')
print('TIPOS DE DADOS / TYPECASTING')
print('===========================================================')

# Variáveis precisam ser definidas em uma só palavra, utilizando underline e sem uso de capitalização
failed_subjects = 2  # inteiro
name = 'John'  # string
price = 2.45  # float
is_going_to_party = True  # booleano
a = 'it\'s'  # a contrabarra é usada para sinalizar que o próximo caracter deve ser incluído na string
print(a)
print(type(failed_subjects))
print(type(name))
print(type(price))
print(type(is_going_to_party))
print('')

# Typecasting é usado para alterar o tipo da variável de forma explícita
print('Your son ' + name + ' is failing ' + str(failed_subjects) + ' subjects.')
print('')

a = int(1)         # 'a' será 1
b = int(2.5)       # b será 2
c = int("3")       # c será 3
c1 = int(float("3.4"))   # é necessário alterar primeiro para floar para mudar para inteiro depois
d = float(1)       # d será 1.0
e = float(2.5)     # e será 2.5
f = float("3")     # f será 3.0
g = float("4.23")  # g será 4.23
h = str("80s")     # h será 80s
i = str(22)        # 'i' será 22
j = str(3.01)      # j será '3.01'

print([a, b, c, c1, d, e, f, g, h, i, j])
print('')
