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

# o google libera algumas bibliotecas no python para uso em suas APIs

from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# caso haja necessidade de alterar SCOPES, deletar o arquivo 'token.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # remover o read only para liberar permissões

# informações de ID e range de células de uma sheet:
SAMPLE_SPREADSHEET_ID = '1JtB-n7EfXe2MIqQJfh3HOWEuazddilY7KA-EuBQpBQQ'  # pegar a id da sheet na url, depois do 'd/'
SAMPLE_RANGE_NAME = 'Página1!A1:C14'  # nomedapagina!rangedecélulas


def main():

    # bloco que realiza o login por meio do token de autenticação
    creds = None

    # o arquivo 'token.json' armazena o acesso do usuário e atualiza o token, é criado automaticamente quando o fluxo
    # de autorização é executado pela primeira vez
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)  # realizando o login

    # se não existem credenciais válidas disponíveis, deixa o usuário logar.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '7credenciais.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # salva as credenciais para um próximo login
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # bloco para execução de comandos da planilha
    try:
        service = build('sheets', 'v4', credentials=creds)  # cria um serviço

        # chama a API do google sheets
        sheet = service.spreadsheets()

        # LEITURA:
        # sheet.values().get() pega informações da planilha
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        print(result)  # retorna um dicionario como informacoes gerais e os dados linha a linha em uma lista
        valores = result['values']  # pegando somente a lista contendo os valores
        print(valores)

        # ESCRITA
        # necessario criar uma lista de listas contendo valores a adicionar
        valores_adicionar = [
            ['dezembro', 'R$ 5.200,00'],
            ['janeiro', 'R$ 56.300,00'],
        ]

        # a chamada do update leva mais parametros, estao descritos na documentacao da API
        # escrevendo novos valores a partir da linha A13
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="A13",
                                       valueInputOption="USER_ENTERED", body={'values': valores_adicionar}).execute()

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

        # Realizando a escrita na planilha
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="C1",
                                       valueInputOption="USER_ENTERED", body={'values': valores_adicionar}).execute()

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
