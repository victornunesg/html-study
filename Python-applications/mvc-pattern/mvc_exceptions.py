# arquivo criado para tratar exceções do código 'basic-backend.py'

# classe para tratar a tentativa de inserção de dados duplicados
class ItemAlreadyStored(Exception):
    pass


# classe para tratar a tentativa de leitura de dados inexistentes
class ItemNotStored(Exception):
    pass
