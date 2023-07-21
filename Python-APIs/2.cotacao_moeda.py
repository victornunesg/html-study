import requests  # usada para buscar a requisição/informação de um site
import json  # usada para tratar a requisição que virá no formato JSON
import matplotlib.pyplot as plt  # usada para exibir o gráfico

# pegando a cotação atual de todas as moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
# print(cotacoes)  # requisição recebe uma resposta 200 (OK)
cotacoes_dic = cotacoes.json()  # cria um dicionário python para cotações usando o método .json()
# print(cotacoes_dic)

# Qual foi a última cotação do Dólar, do Euro e do BitCoin?
print(f'Cotação do dólar: R$ {cotacoes_dic["USD"]["bid"]}')
print(f'Cotação do euro: R$ {cotacoes_dic["EUR"]["bid"]}')
# print(f'Cotação do bitcoin: R$ {cotacoes_dic["BTC"]["bid"]}')

# Pegar a cotação dos últimos 30 dias do dólar
dolar_request = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
dolar_dic = dolar_request.json()
dolar_dic = [float(item['bid']) for item in dolar_dic]
# print(dolar_dic)

# Pegar as cotações do BitCoin de Jan/20 a Out/20
# btc_request = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031')
# btc_dic = btc_request.json()
# btc_dic = [float(item['bid']) for item in btc_dic]
# btc_dic.reverse()  # invertendo a ordem dos valores (agora estarão ordenados do mais antigo para o mais recente)
# print(btc_dic)

# Gráfico com as cotações do BitCoin
# plt.figure(figsize=(15, 5))
# plt.plot(btc_dic)
# plt.show()
