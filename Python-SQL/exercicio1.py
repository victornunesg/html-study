"""" EXERCÍCIO DESAFIO

Elaborar um relatório da análise dos salários da unidade de San Francisco da empresa.
O objetivo é entender:

    1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)
    2. Quantos funcionários tivemos ao longo dos anos
    3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)

Base de dados a ser usada: salarios.sqlite """

import pyodbc
import pandas as pd
import sqlite3

# print('\n===========================================================')
# print('BLOCO DE CONEXÃO COM O BANCO DE DADOS - PYODBC')
# print('===========================================================')
#
# dados_conexao = ("Driver={SQLite3 ODBC Driver};"
#                  "Server=localhost;"
#                  "Database=salarios.sqlite")
#
# conexao = pyodbc.connect(dados_conexao)
# print('\nConexão bem sucedida!')
#
# # criando o cursor, é quem vai executar os códigos SQL no banco
# cursor = conexao.cursor()
#
# # pegando todas as informações da tabela
# cursor.execute("SELECT * from Salaries")
# valores = cursor.fetchall()  # todos valores da tabela
# descricao = cursor.description  # descrição geral da tabela
#
# # colunas = [tupla[0] for tupla in descricao]
# colunas = []
# for item in descricao:
#     colunas.append(item[0])
# print(colunas)

# cursor.close()
# conexao.close()

print('\n===========================================================')
print('BLOCO DE CONEXÃO COM O BANCO DE DADOS - SQLITE3')
print('===========================================================')

# como o sqlite3 já vem instalado/configurado no python, não é necessário passar os dados de conexão
conexaosqlite = sqlite3.connect('salarios.sqlite')
cursorsqlite = conexaosqlite.cursor()

# pegando todas as informações da tabela
cursorsqlite.execute("SELECT * from Salaries")
valores = cursorsqlite.fetchall()  # todos valores da tabela
descricao = cursorsqlite.description  # descrição geral da tabela

tabela_salarios1 = pd.read_sql('SELECT * FROM Salaries WHERE Agency = "San Francisco"', conexaosqlite)
# print(type(tabela_salarios1))
# print(tabela_salarios1)

# obtendo as colunas da tabela
colunas = [item[0] for item in descricao]  # usando for em como list comprehension
# print(colunas)

# obtendo o mesmo resultado (dados em tabela) usando o método 'from_records' do pandas
tabela_salarios = pd.DataFrame.from_records(valores, columns=colunas)
# print(type(tabela_salarios))
# print(tabela_salarios)

# garantindo que estamos olhando apenas para 'San Francisco', filtrando com loc, recebe linhas e colunas como argum.
# equivalente ao select da linha 60
tabela_salarios = tabela_salarios.loc[tabela_salarios["Agency"] == "San Francisco", :]  # todas as colunas


print("1. Qual foi a evolução do salário médio ao longo dos anos?")

# groupby do pandas, agrupa os dados de acordo com a coluna, já o mean() calcula a média
tabela_salarios_media = tabela_salarios.groupby("Year").mean("TotalPay")
print(tabela_salarios_media)

print("\n2. Quantos funcionários tivemos ao longo dos anos?")
tabela_salarios_func = tabela_salarios.groupby("Year").count()
# passando dentro de dois colchetes para o pandas reconhecer como dataframe, e nao como uma serie de dados
print(tabela_salarios_func[["Id"]])
# renomeando as colunas atraves do rename (recebe uma lista de dicionarios)
tabela_salarios_func = tabela_salarios_func.rename(columns={"Id": "Qtde"})

print("\n3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)?")


def formatar(valor):
    return 'R${:,.2f}'.format(valor)


tabela_salarios_gasto = tabela_salarios.groupby("Year").sum("TotalPay")

# aplicando a função de formatação dos valores definida acima nas colunas de interesse
tabela_salarios_gasto["TotalPay"] = tabela_salarios_gasto["TotalPay"].apply(formatar)
tabela_salarios_gasto["TotalPayBenefits"] = tabela_salarios_gasto["TotalPayBenefits"].apply(formatar)

print(tabela_salarios_gasto[["TotalPay", "TotalPayBenefits"]])




cursorsqlite.close()
conexaosqlite.close()
