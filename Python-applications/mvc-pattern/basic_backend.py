"""Para entender como o MVC funciona, vamos implementar um aplicativo CRUD (Create, Read, Update, Delete) simples.

Vamos pensar no estoque de uma pequena mercearia. Uma lista de produtos típica ficaria assim:

Nome	Preço	Quantidade
Pão	     0,5	    20
Leite	 1,0	    10
Vinho	 10,0	     5

Iremos representar por uma lista de dicionários

IMPORTANTE!
Trataremos as exceções dessa implementação no arquivo à parte 'mvc-exceptions' pois aqui não há controle de entrar com
dados duplicados ou entrar com dados inexistentes. Caso não fossem tratadas, teríamos problemas em produção."""

import mvc_exceptions as mvc_exc  # importando as exceções (classes) definidas no arquivo mvc_exceptions.py

# Usaremos uma variável global para armazenar a lista pois seu estado deve ser compartilhado por todas as operações
items = list()  # criando uma lista vazia, usaremos como variável global

# print('\n===========================================================')
# print('FUNCIONALIDADE CRIAR/CREATE')
# print('===========================================================')

# irão apenas acrescentar novos dados na lista global, não retornam nada.


# função para atribuir uma lista existente (my_items por exemplo) na nossa liste 'items'
def create_items(app_items):
    global items
    items = app_items


# função para atribuir item a item do estoque na nossa liste 'items'
def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))  # verifica se o item já existe na lista
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))  # chama a exceção de duplicado
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})  # acrescenta item na lista


# print('\n===========================================================')
# print('FUNCIONALIDADE LER/READ')
# print('===========================================================')


# ler um item específico da lista
def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        # chamando a exceção de item inexistente
        raise mvc_exc.ItemNotStored('Can\'t read "{}" because it\'s not stored'.format(name))


# retorna todos os itens da lista
def read_items():
    global items
    return [item for item in items]


# print('\n===========================================================')
# print('FUNCIONALIDADE ATUALIZAR/UPDATE')
# print('===========================================================')


def update_item(name, price, quantity):
    global items
    # i_x é uma tupla, idxs_items é uma lista de tuplas
    # essa função retorna uma lista contendo uma tupla que traz o índice e o dicionário do item 'name', da busca do item
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        # fazendo o unpacking da tupla pra poder separar o item e o índice a ser atualizado
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        # caso não encontre, chama a exceção de item inexistente
        raise mvc_exc.ItemNotStored('Can\'t update "{}" because it\'s not stored'.format(name))


# print('\n===========================================================')
# print('FUNCIONALIDADE EXCLUIR/DELETE')
# print('===========================================================')


def delete_item(name):
    global items
    # mesma lógica da funcionalidade de atualização
    idxs_items = list(filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored('Can\'t delete "{}" because it\'s not stored'.format(name))


# print('\n===========================================================')
# print('TESTANDO O APP')
# print('===========================================================')
#
#
# def main():
#
#     my_items = [
#         {'name': 'bread', 'price': 0.5, 'quantity': 20},
#         {'name': 'milk', 'price': 1.0, 'quantity': 10},
#         {'name': 'wine', 'price': 10.0, 'quantity': 5},
#     ]
#
#     # CREATE
#     create_items(my_items)
#     create_item('beer', price=3.0, quantity=15)
#     # if we try to re-create an object we get an ItemAlreadyStored exception
#     # create_item('beer', price=2.0, quantity=10)
#
#     # READ
#     print('READ items')
#     print(read_items())
#     # if we try to read an object not stored we get an ItemNotStored exception
#     # print('READ chocolate')
#     # print(read_item('chocolate'))
#     print('READ bread')
#     print(read_item('bread'))
#
#     # UPDATE
#     print('UPDATE bread')
#     update_item('bread', price=2.0, quantity=30)
#     print(read_item('bread'))
#     # if we try to update an object not stored we get an ItemNotStored exception
#     # print('UPDATE chocolate')
#     # update_item('chocolate', price=10.0, quantity=20)
#
#     # DELETE
#     print('DELETE beer')
#     delete_item('beer')
#     # if we try to delete an object not stored we get an ItemNotStored exception
#     # print('DELETE chocolate')
#     # delete_item('chocolate')
#
#     print('READ items')
#     print(read_items())



