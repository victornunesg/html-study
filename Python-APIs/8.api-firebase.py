# Criar o projeto no Firebase
""" Criar conta no google, logar no firebase e começar um projeto do zero no console
Ir no menu Criação > RealTime Database para criar BD em tempo real
Selecionar modo de teste e ativar, criar itens no banco de dados para simular um sistema de vendas"""

# Link documento REST API Firebase
# https://firebase.google.com/docs/reference/rest/database

# Criar o Database (atenção às regras de segurança)
# Estrutura de árvore

# Interação com o Database (REST API)
import requests
import json

link = "https://testeapipython-979c1-default-rtdb.firebaseio.com/"  # link do banco de dados do firebase

# Criar uma venda (POST)
dados = {'cliente': 'alon', 'preco': 150, 'produto': 'teclado'}  # dicionário em formato json, respeitando a estrutura do BD do firebase
requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))  # esse ultimo parametro transforma o dicionario do python em um texto no formato json
print(requisicao)  # verificando a resposta da requisição
print(requisicao.text)  # se der erro, exibe a mensagem de erro e se der certo (resposta 200), retorna o ID da venda

# Criar um novo produto (POST)
dados = {'nome': 'teclado', 'preco': 150, 'quantidade': 80}
requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Editar a venda (PATCH)
dados = {'cliente': 'lira'}
requisicao = requests.patch(f'{link}/Vendas/-MyJSm_N0S8KhCc3nAku/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)

# Pegar uma venda específico ou todas as vendas (GET)
requisicao = requests.get(f'{link}/Vendas/.json')  # filtrando apenas a 'tabela' de vendas do banco de dados
print(requisicao)
dic_requisicao = requisicao.json()  # transforma a resposta em texto (json) em um dicionário python
print(dic_requisicao)
id_alon = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "victor":
        print(id_venda)
        id_alon = id_venda

# Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_alon}/.json')
print(requisicao)
print(requisicao.text)
