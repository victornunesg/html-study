import requests  # usada para buscar a requisição/informação de um site
import json  # usada para tratar a requisição que virá no formato JSON

# pegando a cotação atual de todas as moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
print(cotacoes)  # requisição recebe uma resposta 200 (OK)
cotacoes_dic = cotacoes.json()  # cria um dicionário python para cotações usando o método .json()
print(cotacoes_dic)

# Qual foi a última cotação do Dólar, do Euro e do BitCoin?
