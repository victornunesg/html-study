""" Python e API

O que é uma API?

É um conjunto de códigos para usar um serviço/site/aplicativo específico. Cada site/ferramenta tem sua própria API.
É importante que você saiba ler as APIs que precisar para saber usar

Um dos padrões mais comuns em API é pegar informações em formato json, uma espécie de dicionário que precisa ser tratada
no Python para podermos analisar

As possibilidades de API são infinitas, vamos fazer 2 exemplos aqui: Cotação de Moedas e Envio de SMS.

Sites como Google, Youtube, Facebook, Twitter, ArcGis e praticamente qualquer ferramenta/site grande tem uma API.

O que precisamos:
Quase sempre você precisa de uma conta para consumir uma API. Algumas APIs são abertas, como a
https://docs.awesomeapi.com.br/api-de-moedas , mas em muitos casos (como veremos no caso do SMS) vamos precisar ter uma
conta ativa para consumir a API

A Documentação da API (ou exemplos da internet) é a chave para conseguir usar uma API"""

import requests  # usada para buscar a requisição/informação de um site
import json  # usada para tratar a requisição que virá no formato JSON

# pegando a cotação atual de todas as moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
print(cotacoes)  # requisição recebe uma resposta 200 (OK)
cotacoes_dic = cotacoes.json()  # cria um dicionário python para cotações usando o método .json()
print(cotacoes_dic)

""" OBSERVAÇÃO
A requisição JSON vem em um formato de dicionário, porém não é o mesmo dicionário do Python o qual conseguimos
manipular facilmente.

Desta forma, temos que transformá-lo em um dicionário Python com o método .json()
"""