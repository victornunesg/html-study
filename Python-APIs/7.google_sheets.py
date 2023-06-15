"""
1a parte: configuração do google sheets - descrito em: 'https://developers.google.com/sheets/api/quickstart/python?hl=pt-br'
    - Habilitar a API do google sheets na sua conta google
        "https://console.cloud.google.com/apis/dashboard?hl=pt-br&pli=1&project=tribal-datum-111915"
    - Criar um projeto
    - Pesquisar na barra de busca 'Google Drive API' e ativar
    - Pesquisar na barra de busca 'Google Sheets API' e ativar
    - Gerar token de autenticação 'Menu > APIs e Serviços > APIs e Serviços Ativados > Tela de permissão OAuth'
    - Selecionar usuário externo, preencher dados obrigatórios na etapa 1, salvar e continuar
    - Na etapa 2, adicionar escopo apenas se desejar limitar algo, caso contrário podemos avançar para etapa 3
    - Na etapa 3, adicionar usuários de teste, salvar e continuar
    - Na sequência, ir em 'credenciais' no menu esquerdo > Criar Credenciais > ID do cliente OAuth
        Tipo de aplicativo = App para computador
    - Fazer o download do JSON, pegar o arquivo na pasta, alterar o nome para 'credenciais.json' e coloca no mesmo local do código

2a parte: utilizando a API do google sheets"""

# O google libera algumas bibliotecas no python para uso em suas APIs

from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # remover o read only para liberar permissões

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1JtB-n7EfXe2MIqQJfh3HOWEuazddilY7KA-EuBQpBQQ'  # pegar a id da sheet na url, depois do 'd/'
SAMPLE_RANGE_NAME = 'Página1!A1:C14'  # class data é o nome da página, definir o intervalo de acordo com sua planilha


def main():

    # bloco que realiza o login por meio de token de autenticação
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '7credenciais.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # executa comandos na planilha
    try:
        service = build('sheets', 'v4', credentials=creds)  # cria um serviço

        # Chama a API do google sheets
        sheet = service.spreadsheets()
        # sheet.values().get() pega informações da planilha
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        print(result)  # retorna um dicionario como informacoes gerais e os dados linha a linha em uma lista

        valores = result['values']
        print(valores)

        # escrevendo novos valores a partir da linha A13
        # necessario criar uma lista de listas contendo valores a adicionar
        valores_adicionar = [
            ['dezembro', 'R$ 5.200,00'],
            ['janeiro', 'R$ 56.300,00'],
        ]
        # a chamada do update leva mais parametros, estao descritos na documentacao da API
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="A13", valueInputOption="USER_ENTERED",
                                       body={'values': valores_adicionar}).execute()

        # adicionando uma nova coluna como um resultado de operacao das duas primeiras colunas
        valores_adicionar = [
            ['Imposto'],
        ]

        # percorrendo a lista de valores (linha 72) para calcular o imposto
        # enumerate serve para pular a primeira linha e nao pegar o string 'Vendas'
        for i, linha in enumerate(valores):
            if i > 0:
                vendas = linha[i].replace('R$', '').replace('.', '')  # tirando o ponto e o R$ do string
                vendas = float(vendas.replace(',', '.'))
                imposto = vendas * 0.1

                # adicionando imposto como uma lista dentro da lista de valores a adicionar
                valores_adicionar.append([imposto])
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="C1", valueInputOption="USER_ENTERED",
                                       body={'values': valores_adicionar}).execute()

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
