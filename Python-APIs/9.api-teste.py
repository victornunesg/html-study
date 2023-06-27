import requests
import json

url = 'https://wsconsultagcc.abrtelecom.com.br/consultagcc'

headers = {"Content-Type": "application/json;charset=UTF-8", "token": "###"}

# data = {
#     "cpf": "###",
#     "ddd": ##,
#     "terminal": ###,
#     "flagPos": 1,
#     "flagPre": 1,
# }


class DadosRequisicao:
    def __init__(self, cpf, ddd, terminal):
        self.cpf = cpf
        self.ddd = ddd
        self.terminal = terminal
        self.flagPos = 1
        self.flagPre = 1


for i in range(2):
    cpf1 = input('CPF: ')
    ddd1 = int(input('DDD: '))
    terminal1 = int(input('Terminal: '))
    entrada = DadosRequisicao(cpf1, ddd1, terminal1)
    requisicao = entrada.__dict__
    resposta = requests.post(url, json=requisicao, verify=False, headers=headers)
    print("Código de retorno HTTP: ", resposta.status_code)
    print("JSON Retorno: ", resposta.json())


# dados = DadosRequisicao("###", ##, ####)
# print(type(dados))
# print(dados.__dict__)
# data = dados.__dict__
# print(type(data))
# print(data)
#
# response = requests.post(url, json=data, verify=False, headers=headers)
#
# print("Status Code", response.status_code)
# print("JSON Response ", response.json())
