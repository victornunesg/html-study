print('\n===========================================================')
print('USER INPUT')
print('===========================================================')

user_name = input('Nome: ')
user_age = input('Idade: ')
print('Olá, ' + user_name + '!')
print('Você tem ' + user_age + ' anos de idade!')
print('')

num1 = input('Digite um número: ')
num2 = input('Digite outro número:')
answer = float(num1) + float(num2)
# é necessário realizar um 'cast', alterando o tipo da variável, pois no input automaticamente é setado como string
# caso contrário o resultado será os dois números concatenados
print('O resultado da soma é: ' + str(answer))  # novamente usando o 'cast' para transformar o float em string

print('\nExercício - transformando km em milhas')
user_name = input('Qual é o seu nome? ')
distance_km = input('Digite a distância em km: ')

distance_miles = float(distance_km) / 1.609

print(f'\nOlá, {user_name.title()}! \nA distância é de {distance_km} km ou {round(distance_miles,2)} milhas!')
