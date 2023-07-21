print('\n===========================================================')
print('RANGE()')
print('===========================================================')

""" ESTRUTURA (3 OPÇÕES):
range(tamanho)
range(inicio, fim)
range(inicio, fim, passo) """

# uso mais comum no FOR:
produtos = ['arroz', 'feijao', 'macarrao', 'atum', 'azeite']
estoque = [50, 100, 20, 5, 80]

for i in range(5):
    print('{}: {} unidades em estoque'.format(produtos[i], estoque[i]))

# range com início e fim
print('\n')
for i in range(2, 10):
    print(i)

"""
Exemplo: Modelo Jack Welch da G&E

Classe A: 10% melhor
Classe B: 80% mantém/busca melhorar
Classe C: 10% pior

Quem são os funcionários classe B?
O programa deve exibir os funcionarios entre as posições 2 e 18, pois já está em ordem decrescente.
"""
funcionarios = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro',
                'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo']
vendas = [2750, 1900, 1500, 1200, 1111, 1100, 999, 900, 880, 870, 800, 800, 450, 400, 300, 300, 120, 90, 80, 70]

print('\nFuncionários Classe B')
for i in range(2, 18):
    print('{}: fez {} vendas'.format(funcionarios[i], vendas[i]))

# range com passo
print('')
print(range(0, 100, 10))

for i in range(0, 100, 10):
    print(i)
