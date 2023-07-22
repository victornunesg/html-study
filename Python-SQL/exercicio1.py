"""" EXERCÍCIO DESAFIO

Elaborar um relatório da análise dos salários da unidade de San Francisco da empres.
O objetivo é entender:

    1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)
    2. Quantos funcionários tivemos ao longo dos anos
    3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)

Base de dados a ser usada: salarios.sqlite """

import pyodbc
import pandas as pd
import sqlite3

print('\n===========================================================')
print('BLOCO DE CONEXÃO COM O BANCO DE DADOS - PYODBC')
print('===========================================================')

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=salarios.sqlite")

conexao = pyodbc.connect(dados_conexao)
print('\nConexão bem sucedida!')

# criando o cursor, é quem vai executar os códigos SQL no banco
cursor = conexao.cursor()

# pegando todas as informações da tabela
cursor.execute("SELECT * from Salaries")
valores = cursor.fetchall()  # todos valores da tabela
descricao = cursor.description  # descrição geral da tabela

# colunas = [tupla[0] for tupla in descricao]
colunas = []
for item in descricao:
    colunas.append(item[0])
print(colunas)

cursor.execute("SELECT TotalPay from Salaries")
listasalarios = cursor.fetchall()
print(listasalarios[0:10])

cursor.execute("SELECT TotalPayBenefits from Salaries")
listabeneficios = cursor.fetchall()
print(listabeneficios[0:10])

cursor.close()
conexao.close()

# print('\n===========================================================')
# print('BLOCO DE CONEXÃO COM O BANCO DE DADOS - SQLITE3')
# print('===========================================================')

# # como o sqlite3 já vem instalado/configurado no python, não é necessário passar os dados de conexão
# conexaosqlite = sqlite3.connect('salarios.sqlite')
# cursorsqlite = conexaosqlite.cursor()
#
# # pegando todas as informações da tabela
# cursorsqlite.execute("SELECT * from Salaries")
# valores2 = cursorsqlite.fetchall()  # todos valores da tabela
# descricao2 = cursorsqlite.description  # descrição geral da tabela
#
# colunas2 = []
# for item in descricao2:
#     colunas2.append(item[0])
# print(colunas2)
#
# tabela_salarios = pd.read_sql('SELECT * FROM Salaries', conexaosqlite)
# print(tabela_salarios)
#
# cursorsqlite.close()
# conexaosqlite.close()
