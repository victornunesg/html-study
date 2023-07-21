"""Informações da API em: https://www.alphavantage.co/

Esta API retorna séries temporais de ações ajustadas semanalmente (último dia de negociação de cada semana, abertura
semanal, alta semanal, baixa semanal, fechamento semanal, fechamento semanal ajustado, volume semanal, dividendo
semanal) do patrimônio global especificado, cobrindo mais de 20 anos de dados históricos . """

from zchave_api_acoes import chave_api  # a chave gerada pela API está em arquivo separado, evitando exposição no código
import requests
import pandas as pd  # para ler o arquivo .csv
from io import StringIO  # para transformar o texto da requisição .csv em arquivo .csv

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}'
r = requests.get(url)
# print(r.text)  # toda requisição tem um texto trazendo as informações dessa requisição
data = r.json()
print(data)

# pegando o arquivo .csv para download
url_csv = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol=IBM&apikey={chave_api}&datatype=csv'
r_csv = requests.get(url_csv)
# print(r_csv.text)

# o método StringIO pega o texto da requisição e em arquivo
arquivo_csv = StringIO(r_csv.text)

# transformando o arquivo csv em tabela para ser utilizado no Pandas
tabela = pd.read_csv(arquivo_csv)
print(tabela)

# pegando a cotação diária de 3 ações diferentes (Itaú, Ambev e BB)
acoes = ['ITUB4', 'ABEV3', 'BBAS3']

tabela_compilada = pd.DataFrame()  # método que cria uma tabela vazia do pandas

for acao in acoes:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey={chave_api}&datatype=csv'
    r = requests.get(url)
    tabela = pd.read_csv(StringIO(r.text))
    lista_tabelas = [tabela_compilada, tabela]  # criando a lista de tabelas para juntar todas as informações
    tabela_compilada = pd.concat(lista_tabelas)  # concatena uma lista de tabelas, adicionando registros na tabela compilada

print(tabela_compilada)

# encontrando ativos, ou seja, o nome da ação através do nome da empresa
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=amazon&apikey={chave_api}&datatype=csv'
r = requests.get(url)
tabela = pd.read_csv(StringIO(r.text))
print(tabela)


# trazendo informações de resultado financeiro de uma empresa
# porém, no endpoint não retorna de todas as empresas (possivelmente as que operam nos EUA apenas)
url = f'https://www.alphavantage.co/query?function=EARNINGS&symbol=AMZN&apikey={chave_api}'
r = requests.get(url)
data = r.json()
print(data)
