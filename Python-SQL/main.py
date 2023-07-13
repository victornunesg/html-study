import pyodbc
import pandas as pd
import sqlite3

print(pyodbc.drivers())

# criando uma variável em forma de tupla para criar a conexão com o BD
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"  # endereço do banco de dados
                 "Database=chinook.db")

# # caso o banco de dados tenha login e senha:
# dados_conexao = ("Driver={SQLite3 ODBC Driver};"
#                  "Server=localhost;"  # endereço do banco de dados
#                  "Database=chinook.db"
#                  "UID=login;"
#                  "PWD=senha")

conexao = pyodbc.connect(dados_conexao)
print('conexão bem sucedida')

# criando o cursor, é quem vai executar os códigos SQL no banco
cursor = conexao.cursor()

""" 
Temos duas opções para executar os comandos SQL
    1. Apenas executar comandos SQL que vão rodar no banco
    2. Executar os comandos e armazenar a consulta em uma variável no Python, como um dataframe no pandas por exemplo"""

# CREATE
# os comandos que executam um SQL que editam o banco de dados, é necessário dar um commit para aplicar efetivamente
cursor.execute("""
                INSERT INTO albums (Title, ArtistId)
                VALUES
                ('Seresta 3.0', 10)
                """)
cursor.commit()

# READ
cursor.execute("SELECT * FROM customers")  # pegando informações do banco de dados, se printar resulta em um objeto
valores = cursor.fetchall()  # armazena as informações na variável, em uma lista de tuplas com cada linha da tabela
print(type(valores))  # por se tratar de uma lista, podemos usar os métodos aplicáveis
print(valores[0])  # primeira linha da base de dados

descricao = cursor.description
print(descricao)  # traz informações da tabela em forma de tuplas

colunas = [tupla[0] for tupla in descricao]  # pegando as colunas
print(colunas)

# usando o Pandas para mostrar os dados em forma de tabela
tabela_clientes = pd.DataFrame.from_records(valores)
print(tabela_clientes)

# UPDATE
cursor.execute("""
                UPDATE customers
                SET Email='victor123@gmail.com
                WHERE Email='luisg@embraer.com.br' """)
cursor.commit()

# DELETE
cursor.execute("""
                DELETE FROM albums
                WHERE AlbumId=2 """)
cursor.commit()

cursor.close()
conexao.close()
