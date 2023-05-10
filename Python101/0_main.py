# File to practice - EXERCISES

produtos = ['tv', 'celular', 'geladeira', 'microondas']
estoque = [100, 2000, 75, 90]

produto = input('Insira o nome do produto: ')
if produto in produtos:
    print(f'Quantidade em estoque: {estoque[produtos.index(produto)]} unidades')
else:
    print('Não temos o produto em estoque.')
