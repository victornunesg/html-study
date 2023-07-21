# API do Banco Central
# https://dadosabertos.bcb.gov.br/dataset?res_format=API
# SandBOX da API: https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/aplicacao#!/recursos/informacoes_diarias#eyJmb3JtdWxhcmlvIjp7IiRmb3JtYXQiOiJqc29uIiwiJHRvcCI6MTAwfX0=

# vamos buscar a API de dinheiro em circulação para ter ideia da volumetria de cédulas estao em circulação em certo momento

import requests
import pandas as pd
import pprint

link = "https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?" \
       "$top=100&$orderby=Data%20desc&$format=json"
requisicao = requests.get(link)
informacoes = requisicao.json()
# pprint.pprint(informacoes)

tabela = pd.DataFrame(informacoes['value'])  # criando uma tabela a partir do dicionario de retorno da requisicao

# formatando as colunas da tabela: separador de milhar, cifrão nos valores
# entretanto para fazer cálculos, recomenda-se não formatar a coluna
tabela["Valor"] = tabela["Valor"].map("R${:,.2f}".format)
tabela["Quantidade"] = tabela["Quantidade"].map("{:,}".format)

# print(tabela)

# pegar todas as informações com várias requisições (paginação)
# configuramos o parâmetro 'Primeiro' (neste caso é o 'skip' no endpoint), também conhecido como offset
tabela_final = pd.DataFrame()
pular_indice = 0


# TRABALHANDO COM PAGINAÇÃO EM APIs

# criando um loop infinito para ir rodando as requisições, para apenas quando a requisição voltar com valores vazios
# adiciona 10k linhas a cada iteração, até chegar em 100k linhas
while True:
    link = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={pular_indice}&$orderby=Data%20desc&$format=json'
    requisicao = requests.get(link)
    informacoes = requisicao.json()
    tabela = pd.DataFrame(informacoes["value"])
    if len(informacoes['value']) < 1:
        break

    # acrescenta as informações da iteração na tabela final
    tabela_final = pd.concat([tabela_final, tabela])
    # altera o valor do parâmetro skip, torna-o uma variável, para pegar os próximos 10k registros na próxima requisição
    pular_indice += 10000

print(tabela_final)
