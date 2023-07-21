""" E-COMMERCE
Digamos que você está analisando todas as vendas dos produtos de tecnologia de um e-commerce e quer saber quais foram os
5 produtos que mais venderam (e suas respectivas quantidades de vendas) - ou seja, queremos descobrir um top 3 produtos
de forma simples """

# from collections import Counter
#
# vendas_tecnologia = {'notebook asus': 2450, 'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000,
#                      'ps5': 14300, 'tablet': 1720, 'notebook dell': 17000, 'ipad': 1000, 'tv philco': 2500,
#                      'notebook hp': 1000}
#
# aux = Counter(vendas_tecnologia)
# print(aux.most_common(3))  # retorna uma lista de tuplas com os 3 maiores valores do dicionario

""" EXIBINDO GRAFICOS NO PYTHON Gráficos no Python

Usaremos o módulo Matplotlib.pyplot, que é o módulo mais usado no Python.
Existem outros, como o Seaborn e o Plotly, caso queira ver/usar. Faremos um grafico de vendas, fazendo as alteracoes:
- Adicionar um Label no eixo X ou eixo Y
- Mudar os nomes dos meses
- Ajeitando o Eixo """

# vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
# meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
#
# import matplotlib.pyplot as plt
#
# plt.plot(meses, vendas_meses)
# plt.ylabel('Vendas')
# plt.xlabel('Meses')
# plt.axis([0, 12, 0, max(vendas_meses)+500])
# plt.show()

""" EDIÇÕES DE GRÁFICOS COM MATPLOTLIB """

# #importando o matplotlib para plotar os gráficos
# import matplotlib.pyplot as plt
#
# #importando o módulo numpy para trabalhar com números
# import numpy as np
#
#
# vendas = np.random.randint(1000, 3000, 50)  # gerando 50 números aleatórios entre 1000 e 2999
# meses = np.arange(1, 51)  # definindo um range de 50 meses
#
# # GRÁFICO DE LINHA
# plt.plot(meses, vendas)
# plt.axis([0, 50, 0, max(vendas)+200])  # definindo a escala do eixo X e Y (baseado no maior valor da lista)
# plt.xlabel('Meses')
# plt.ylabel('Vendas')
# plt.show()
#
# # GRÁFICO DE DISPERSÃO
# plt.scatter(meses, vendas)
# plt.show()
#
# # GRÁFICO DE BARRAS
# plt.bar(meses, vendas)
# plt.show()
#
# # MÚLTIPLOS GRÁFICOS NO MESMO PLOT (Para melhor visualização/comparação)
# plt.figure(1, figsize=(15, 3))  # 1 significa apenas 1 linha horizontal de gráficos / figsize é o tamanho deles
# plt.subplot(1, 3, 1)  # 1 linha horizontal, 3 colunas, primeiro gráfico da linha
# plt.plot(meses, vendas, color='red')
# plt.subplot(1, 3, 2) # 1 linha horizontal, 3 colunas, segundo gráfico da linha
# plt.scatter(meses, vendas)
# plt.subplot(1, 3, 3) # 1 linha horizontal, 3 colunas, terceiro gráfico da linha
# plt.bar(meses, vendas)
# plt.show()
