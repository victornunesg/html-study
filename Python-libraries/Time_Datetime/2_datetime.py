# Principais funções do módulo datetime

from datetime import datetime, date
###########################################
print("\nNOW()")
###########################################

# retorna a data e hora atuais, tem vários métodos/atributos para trazer informações de ano, dia, minuto, data, etc.

agora = datetime.now()
print(f'Agora: {agora}')
print(f'Data: {agora.date()}')
print(f'Horário: {agora.time()}')

###########################################
print("\nTODAY()")
###########################################

# retorna apenas a data atual

hoje = date.today()
print(f'Agora: {agora}')


