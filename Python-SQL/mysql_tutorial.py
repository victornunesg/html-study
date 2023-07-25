# instalar primeiro o driver do mysql (pip install mysql-connector-python), vai baixar o driver do mysql e além disso,
# instala a biblioteca do mysql para realizar a integração com o python
import mysql.connector

# conectando com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='842867',
    database='banco'
)
print('conexão bem sucedida')

# criando o cursor para executar os comandos sql
cursor = conexao.cursor()
print('cursor criado')

# CRUD

# CREATE
comando = 'INSERT INTO vendas (nome_produto, valor)' \
          'VALUES ("sucrilhos", 20)'
cursor.execute(comando)  # executa o comando SQL
conexao.commit()  # edita o banco de dados

# READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando)  # executa o comando SQL
resultado = cursor.fetchall()  # leitura do banco de dados
print(resultado)

# UPDATE
comando = 'UPDATE vendas SET valor = 30 WHERE nome_produto = "toddynho"'
cursor.execute(comando)  # executa o comando SQL
conexao.commit()  # edita o banco de dados

# DELETE
comando = 'DELETE FROM vendas WHERE nome_produto = "toddynho"'
cursor.execute(comando)  # executa o comando SQL
conexao.commit()  # edita o banco de dados

cursor.close()
conexao.close()
