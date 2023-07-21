"""" EXERCÍCIO DESAFIO

Elaborar um relatório da análise dos salários da unidade de San Francisco da empres.
O objetivo é entender:

    1. Qual foi a evolução do salário médio ao longo dos anos (TotalPay e TotalPayBenefits)
    2. Quantos funcionários tivemos ao longo dos anos
    3. Qual foi a evolução do total gasto com salário ao longo dos anos (TotalPayBenefits)

Base de dados a ser usada: salarios.sqlite """

import pyodbc
import pandas as pd

print('\n===========================================================')
print('BLOCO DE CONEXÃO COM O BANCO DE DADOS')
print('===========================================================')

dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"
                 "Database=salarios.sqlite")

conexao = pyodbc.connect(dados_conexao)
print('\nConexão bem sucedida!')

# criando o cursor, é quem vai executar os códigos SQL no banco
cursor = conexao.cursor()

cursor.execute("SELECT TotalPay from Salaries")
listasalarios = cursor.fetchall()
somasalarios = 0
# for salario in listasalarios:
#     somasalarios += salario
# media = somasalarios / len(listasalarios)
print(listasalarios[0:10])

cursor.execute("SELECT TotalPayBenefits from Salaries")
listabeneficios = cursor.fetchall()
somabeneficios = sum(listabeneficios)
print(somabeneficios)
# for beneficio in listabeneficios[0:10]:
#     print(beneficio)
# mediabeneficios = somabeneficios / len(listabeneficios)
print(listabeneficios[0:10])


cursor.close()
conexao.close()
