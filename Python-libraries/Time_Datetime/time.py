# Principais funções do módulo time

''' Não é necessária a instalação, ela já vem instalada com o Python'''

import time
import locale  # traduz para português quando usamos a função strftime()

###########################################
print("\nTIME()")
###########################################

# retorna o tempo atual em segundos desde a Epoch (1/1/1970)
tempo_atual_segundos = time.time()
print(f'Tempo atual: {tempo_atual_segundos} segundos desde a Epoch.')

# retorna o tempo atual em nanosegundos desde a Epoch (1/1/1970)
tempo_atual_nanosegundos = time.time_ns()
print(f'\nTempo atual: {tempo_atual_nanosegundos} nanosegundos desde a Epoch.')

# exemplo do uso da biblioteca para controle de desempenho de um programa
inicio = time.time()

for i in range(1_000_000):  # o _ serve apenas para facilitar a leitura do número 1000000
    pass

fim = time.time()
print(f'\nTempo decorrido: {fim-inicio} segundos')

###########################################
print("\nTIME.SLEEP()")
###########################################

# faz o programa esperar pelo número de segundos especificado
print('Iniciando a pausa')
time.sleep(2) #  pausa programada por 2s
print('Pausa terminada')

###########################################
print("\nTIME.CTIME()")
###########################################

# converte um tempo expresso em segundos desde a epoch em uma string representando o tempo local
tempo_em_segundos = time.time()
tempo_local = time.ctime(tempo_em_segundos)
print(f'Tempo local: {tempo_local}')

###########################################
print("\nTIME.LOCALTIME()")
###########################################

# converte um tempo expresso em segundos desde a epoch em um objeto 'struct_time'
# este objeto contém informações sobre o tempo local (ano, mês, dia, hora...)
# a função 'localtime()' usa o fuso horário local
tempo_em_segundos = time.time()
tempo_local = time.localtime(tempo_em_segundos)
print(f'Tempo local: {tempo_local}')  # retorna uma tupla com os dados
print(f'Fuso horário: {tempo_local.tm_zone}')
print(f'Ano: {tempo_local.tm_year}, mês: {tempo_local.tm_mon}, dia: {tempo_local.tm_mday}')

print("")
print(time.time())
print(time.ctime(time.time()))
print(time.localtime())

###########################################
print("\nTIME.STRFTIME()")
###########################################

# converte um objeto 'struct_time' para uma string de acordo com um formato específico (disponíveis na doc)
tempo_em_struct = time.localtime()
print(tempo_em_struct)
print(time.strftime("%d %B %Y", tempo_em_struct))
print(time.strftime("%H: %M: %S", tempo_em_struct))

tempo_formatado = time.strftime("%A, %d de %B de %Y, %H: %M: %S", tempo_em_struct)
print(f'\nTempo formatado: {tempo_formatado}')

# define a localização para português
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # basicamente uma configuração, não preocupar com o detalhe
tempo_em_struct = time.localtime()
tempo_formatado = time.strftime("%A, %d de %B de %Y, %H: %M: %S", tempo_em_struct)
print(f'\nTempo formatado: {tempo_formatado}')

###########################################
print("\nTIME.STRPTIME()")
###########################################

# analisa uma string representando um horário de acordo com um formato. retorna um objeto 'struct_time'

string_tempo = "30 Junho, 2023"
formato = "%d %B, %Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f'Tempo em struct: {tempo_em_struct}')

string_tempo = "06/09/2023"
formato = "%d/%m/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f'Tempo em struct (BRASIL): {tempo_em_struct}')

string_tempo = "06/09/2023"
formato = "%m/%d/%Y"
tempo_em_struct = time.strptime(string_tempo, formato)
print(f'Tempo em struct (EUA): {tempo_em_struct}')

###########################################
print("\nTIME.GMTIME()")
###########################################

# converte um tempo expresso em segundos desde a epoch em um objeto 'struct_time' em UTC (Coordinated Universal Time)
# UTC é também conhecido como GMT (Greenwich Mean Time). É o fuso horário padrão em que as funções 'time' operam

print(time.gmtime(0))  # tempo em UTC para 0 segundos desde a epoch

gmt_struct = time.gmtime()  # tempo atual em UTC já que não fornecemos nenhum argumento
print(f'Tempo em UTC: {gmt_struct}')
print(f'Tempo local: {time.localtime()}')  # pega o fuso horário local comparando com a UTC // GMT-3 no caso
print(f'Tempo em UTC formatado via STRFTIME(): {time.strftime("%A, %d de %B de %Y, %H:%M:%S", gmt_struct)}')

gmt_struct_exemplo = time.gmtime(1234567890)  # tempo em UTC para 1234567890 segundos desde a epoch
print(f'\nTempo em UTC: {gmt_struct_exemplo}')
print(f'Tempo em UTC formatado via STRFTIME(): {time.strftime("%A, %d de %B de %Y, %H:%M:%S", gmt_struct_exemplo)}')

###########################################
print("\nTIME.MKTIME()")
###########################################

# converte um objeto 'struct_time' em segundos desde a epoch, é o inverso da função localtime().
# podemos converter o objeto 'struct_time' retornado pela função localtime() usando a função mktime().
# o resultado deve ser o mesmo que o valor retornado pela função time()

tempo_em_struct = time.localtime()
tempo_em_segundos = time.mktime(tempo_em_struct)
print(f'Tempo em segundos: {tempo_em_segundos}')
print(f'Tempo em segundos: {time.time()}')

# usando o método mktime para calcular a diferença entre dois tempos
tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2023, 1, 1, 0, 0, 0, 0, 0, 0))  # passando uma tupla ordenada, na estrutura do 'struct_time', para 01/01/2023
diferenca = time.mktime(tempo_atual) - tempo_ano_novo
print(f'\nDiferença em segundos: {diferenca}')
