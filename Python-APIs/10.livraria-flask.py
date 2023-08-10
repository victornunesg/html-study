""" API para gerenciamento de acervo de livros - FLASK/POSTMAN
1. Objetivo: criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
2. URL Base: localhost
3. Endpoints:
    - localhost/livros (GET) - trazer todos os livros
    - localhost/livros (POST) - adicionar livro
    - localhost/livros/id (GET) - trazer livro por id
    - localhost/livros/id (PUT) - modificar livro por id
    - localhost/livros/id (DELETE) - deletar livro por id
4. Recursos: acervo de livros

APRIMORAR PARA USAR BANCO DE DADOS """

# jsonify nos auxilia com o retorno no formato JSON (esperado quando se trata de APIs)
# request para acesso aos dados transitados durante as requisições
from flask import Flask, jsonify, request

# instalando o driver e a biblioteca do mysql para integração com o python
import mysql.connector  # pip install mysql-connector-python

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
# por padrão, o flask ordena os campos do response por ordem alfabética, estamos desabilitando isso

# por hora os dados serão armazenados simplesmente em uma lista de dicionarios
livros = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'Hábitos Atômicos',
        'autor': 'James Clear'
    }
]


# Consultar (todos)
@app.route('/livros', methods=['GET'])  # garante que só o método GET será utilizado
def obter_livros():
    return jsonify(mensagem="Lista de livros.", dados=livros)  # devolvendo o dicionário em JSON


# Consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(mensagem="Resultado da busca.", dados=livro)


# Adicionar
@app.route('/livros', methods=['POST'])
def adicionar_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(mensagem="Livro cadastrado com sucesso.", dados=livros)


# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro(id):
    livro_editado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_editado)
            return jsonify(livros[indice])


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


app.run(host='localhost', debug=True)
