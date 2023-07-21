# passo a passo

# ======================================
# 1: importar a base de dados
# ======================================
import pandas
import plotly.express  # sempre quando importar colocar o express

# para bases que tenham caracteres especiais, tem que informar o encoding
tabela = pandas.read_csv("clientes.csv", encoding="latin", sep=";")

# ======================================
# 2: visualizar a base de dados
# ======================================
print(tabela)
# entender as informações disponíveis
# procurar erros na base de dados

# ======================================
# 3: tratamento de dados
# ======================================

# deletar colunas inuteis, pois deve-se tirar tudo o que nao sera usado para nao atrapalhar analise
# axis=0 se for linha, axis=1 se for coluna
tabela = tabela.drop("NOME DA COLUNA", axis=1)

# acertar informacoes que estao sendo reconhecidas de forma errada (texto deve ser texto, num deve ser num)
# corrigir informacoes vazias
# o comando info mostra o detalhamento geral da tabela, mostra informacoes vazias e o tipo de dado de cada coluna
print(tabela.info())  # int = numerico // object = texto

# converte o tipo da coluna para numerico
# podendo forcar celulas que nao sao numericas serem convertidas com o 'coerce' (vai virar NaN)
# ou voce pode ignorar o erro optando por 'ignore'
tabela["NOME DA COLUNA"] = pandas.to_numeric(tabela["NOME DA COLUNA"], errors="coerce")
tabela["NOME DA COLUNA"].astype(str)  # converte para texto

print(tabela[tabela["NOME DA COLUNA"].isna()])  # mostra as linhas que possuem valores vazios para a coluna selecionada
tabela = tabela.dropna()  # joga fora linhas que tem valores vazios

print(tabela.info())  # verificando se o tratamento de dados deu certo

# ======================================
# 4: analise inicial para entender notas dos clientes
# ======================================

print(tabela.describe())  # descreve as colunas da tabela, qtos valores, media, minimo, maximo

# palpites:
# quanto maior o salario, maior a nota
# clientes de promocao sao piores

# instalar o plotly para usar graficos para analise

# criar grafico, mostrando no x a origem e no y as notas, calculando a media (padrao seria soma) e coloca label text
grafico = plotly.express.histogram(
    tabela, x="NOME DA COLUNA EIXO X", y="NOME DA COLUNA EIXO Y", histfunc="avg", text_auto=True)

# exibe grafico
grafico.show()

# ======================================
# 5: analise completa para entender como cada caracteristica do cliente impacta na nota
# ======================================

# gerando um grafico para cada coluna da tabela usando um loop for
# nbins controla o total de agrupamentos por grafico
for coluna in tabela.columns:
    grafico = plotly.express.histogram(
        tabela, x=coluna, y="Nota (1-100)", histfunc=avg, text_auto=True, nbins=5)
    grafico.show()

# PERFIL IDEAL DE CLIENTE
# acima de 15 anos (n'ao tem muita diferenca nas faixas etarias depois disso)
# faixa salarial nao parece fazer tanta diferenca
# areas de trabalho: entretenimento e artista
# tem entre 10 e 15 anos de experiencia
# com familias nao tao grandes (maximo 7 pessoas)
