import pyodbc  # biblioteca que permite integração com os mais diversos bancos de dados (SQL, POSTGRES, ETC)
import pandas as pd

print(pyodbc.drivers())  # verifica quais os drivers estão instalados na máquina

# driver do pyodbc: http://www.ch-werner.de/sqliteodbc/

print('\n===========================================================')
print('BLOCO DE CONEXÃO COM O BANCO DE DADOS')
print('===========================================================')

# criando uma variável em forma de tupla para criar a conexão com o BD
# caso o banco tenha login e senha, passar também como parâmetros - UID (login) / PWD (senha)
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
                 "Server=localhost;"  # endereço do banco de dados
                 "Database=chinook.db")

# cria a conexão com o BD
conexao = pyodbc.connect(dados_conexao)
print('\nConexão bem sucedida!')

# criando o cursor, é quem vai executar os códigos SQL no banco
cursor = conexao.cursor()

print('\n===========================================================')
print('CREATE')
print('===========================================================')

cursor.execute("""  INSERT INTO albums (Title, ArtistId)
                    VALUES
                    ('Seresta 3.0', 10) """)
# os comandos que executam um SQL onde há edição no banco de dados, é necessário dar um commit para aplicar efetivamente
cursor.commit()
print("\n Dados inseridos com sucesso na tabela 'albums' ")

print('\n===========================================================')
print('READ')
print('===========================================================')

cursor.execute("SELECT * FROM customers")  # pegando informações do banco de dados, se printar resulta em um objeto
valores = cursor.fetchall()  # armazena as informações na variável, em uma lista de tuplas com cada linha da tabela

print(f"Tipo do cursor: {type(valores)}")  # por se tratar de uma lista, podemos usar os métodos aplicáveis
print(f"3 primeiros valores: {valores[0:3]}")  # três primeiras linhas da base de dados

descricao = cursor.description
print(f"\nDescricao do cursor: {descricao}")  # traz informações da tabela em forma de tuplas

colunas = [tupla[0] for tupla in descricao]  # pegando as colunas (usando list comprehension)
print(f"\nColunas da tabela do banco: {colunas}\n")

# usando o Pandas para mostrar os dados em forma de tabela
tabela_clientes = pd.DataFrame.from_records(valores[0:10])
print(tabela_clientes)

print('\n===========================================================')
print('UPDATE')
print('===========================================================')

cursor.execute("""
                UPDATE customers
                SET Email='victor123@gmail.com
                WHERE Email='luisg@embraer.com.br' """)
cursor.commit()
print("\n Dados atualizados com sucesso na tabela 'customers' ")

print('\n===========================================================')
print('DELETE')
print('===========================================================')

cursor.execute("""
                DELETE FROM albums
                WHERE AlbumId=2 """)
cursor.commit()
print("\n Dados deletados com sucesso na tabela 'albums' ")

cursor.close()
conexao.close()
