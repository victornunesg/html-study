""" Python e API com Login

O 1º Passo de toda API com Login é criar uma conta e pegar suas credenciais
No seu código, o 1º passo é sempre estabelecer a conexão com a API, usando seu login e suas credenciais
Como cada API é uma ferramenta diferente, cada uma delas pode exigir que você faça algum tipo de configuração, que vai estar explicada na API. No nosso caso, teremos que validar um número e criar um número de envio

Depois, usamos os métodos da API normalmente para fazer o que queremos. No nosso caso, enviar um SMS

1. Vamos criar um login no Twilio¶
https://www.twilio.com/docs/libraries/python

2. Depois do Login, vamos pegar 3 informações:
    ID da Conta
    Token
    Número de Envio

3. Agora vamos validar um número porque no Twilio, enviar SMS para um número válido é de graça

4. Agora podemos fazer o nosso código de acordo com as orientações do Twilio


RECOVERY CODE: heJ3hCd7Kh9R4nj5brcQUZpYf9KS57lNH-7lxrEz"""

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# SID: ACbade097588007374e1839cb7e55aefc0
# Token: 1c64818de0320d8f5c93a726732410a8

account_sid = 'ACbade097588007374e1839cb7e55aefc0'
auth_token = '1c64818de0320d8f5c93a726732410a8'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Teste de envio SMS via Python e Twilio.",
                     from_='+13613155385',  # numero trial criado pelo twilio
                     to='+5561999350868'
                 )

print(message.sid)
