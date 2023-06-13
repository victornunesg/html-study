import requests
import json
import pandas as pd

opcao = int(input('Digite 1 para consultar pelo CEP\n'
                  'Digite 2 para consultar pelo endereco\n'
                  'Ou pressione qualquer tecla para sair: '))
if opcao == 1:
    cep = input('Insira o CEP para consultar endereço: ')
    cep = cep.replace('.', '').replace('-', '').replace(' ', '')

    while len(cep) != 8:
        print('\nTamanho inválido!')
        cep = input('Insira o CEP para consultar endereço: ')
        cep = cep.replace('.', '').replace('-', '').replace(' ', '')

    endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    endereco_dic = endereco.json()
    for item, valor in endereco_dic.items():
        print(f'{str(item).capitalize()}: {valor}')
elif opcao == 2:
    uf = input('Insira a UF: ')
    cidade = input('Insira a Cidade: ')
    logradouro = input('Insira o Logradouro: ')

    while len(cidade) <3 or len(logradouro) < 3:
        print('\nTamanho inválido!')
        uf = input('Insira a UF: ')
        cidade = input('Insira a Cidade: ')
        logradouro = input('Insira o Logradouro: ')
    endereco = requests.get(f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/')
    endereco_dic = endereco.json()
    print('\nSegue abaixo as correspondências encontradas:')
    tabela = pd.DataFrame(endereco_dic)
    print(tabela)
else:
    pass
