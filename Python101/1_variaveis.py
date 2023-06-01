print('\n===========================================================')
print('COMANDO PRINT E FLUXO DO CÓDIGO/PROGRAMA')
print('===========================================================')

print('Bem-vindo ao Python 101!')
# ' ou " podem ser usados como entrada de texto
# O fluxo do programa roda de cima para baixo, esquerda para direita
print('Essa é a segunda linha')
print('')

print('\n===========================================================')
print('VARIÁVEIS')
print('===========================================================')

failed_subjects = "2"
name = 'John'
print('Dear Mrs Badger')
print('Your son ' + name + ' is failing ' + failed_subjects + ' subjects.')
print(name + '  will need to redo ' + failed_subjects + '  courses.')
name = 'Eric'  # Variáveis podem ser atualizadas a qualquer momento no programa
print(name + '  is doing well in geography.')

print('\n===========================================================')
print('TIPOS DE VARIÁVEL')
print('===========================================================')

"""
Uma variável é um objeto, afinal tudo é um objeto em Python

int -> inteiro<br>
string -> texto<br>
float -> números com casas decimais (ponto flutuante)<br>
bool ou boolean -> True ou False<br>

Obs: Variáveis em Python não são declaradas explicitamente, mas isso não significa que deve-se ficar mudando otempo todo
Obs2: Cuidado com os nomes restritos
"""
faturamento = 1000
print(type(faturamento))

faturamento = 1000.00
print(type(faturamento))

faturamento = '1.000'
print(type(faturamento))

ganha_bonus = True
print(type(ganha_bonus))

print('\n===========================================================')
print('COMANDO FORMAT')
print('===========================================================')

faturamento = 2000
custo = 500
lucro = faturamento - custo

# Variáveis sendo utilizadas no print, concatenando textos:
print('O faturamento da loja foi ' + str(faturamento) + '. O custo da loja foi ' + str(custo) +
      '. Assim, o lucro da loja foi de ' + str(lucro))

# Variáveis sendo utilizadas no print, Comando FORMAT:
print('O faturamento da loja foi {}. O custo da loja foi {}. Assim, o lucro da loja foi de {}'.format(faturamento,
                                                                                                      custo,
                                                                                                      lucro))

print('\n===========================================================')
print('F-STRING')
print('===========================================================')
faturamento = 1000
custo = 400

lucro = faturamento - custo

# com format
print("O faturamento foi de {} e o lucro de {}".format(faturamento, faturamento - custo))

# com f-string
print(f"O faturamento foi de {faturamento} e o lucro de {faturamento - custo}")

print('\n===========================================================')
print('MUDANÇA DE TIPO DE VARIÁVEL')
print('===========================================================')

faturamento = float(input("Insira o faturamento"))
custo = float(input("Insira o custo"))

print(type(faturamento))
print(type(custo))

lucro = faturamento - custo

print(lucro)

# str -> muda para string
# int -> muda para inteiro
# float -> muda para float