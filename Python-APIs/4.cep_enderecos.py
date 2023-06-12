import requests
import json

endereco = requests.get('viacep.com.br/ws/71937720/json/')
print(endereco)
endereco_dic = endereco.json()
print(endereco_dic)
