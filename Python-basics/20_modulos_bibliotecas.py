print('\n===========================================================')
print('MÓDULOS E BIBLIOTECAS')
print('===========================================================')

""" IMPORTÂNCIA
Já tem muita coisa pronta, então você não precisa criar do zero.
Se você souber usar Módulos e como usar um módulo novo, você vai conseguir fazer praticamente tudo no Python

ESTRUTURA BÁSICA -  Sempre comece o código importando os módulos (devem ser declarados antes, no início)
import módulo
ou
import módulo as nome 

EXEMPLO - abrindo o um site no browser usando o módulo webbrowser:

import webbrowser as wb
wb.open('https://hashtagtreinamentos.com')

VARIAÇÕES
#importar o módulo sem precisar usar o nome dele
from modulo import *

#importar apenas algumas partes do módulo
from modulo import funcao1, funcao2, etc.

Referência: https://docs.python.org/3/py-modindex.html """

# importando módulo platform
import platform

# podemos dar um apelido ao módulo importado, abreviando ou deixando mais intuitivo:
import platform as pl

# também podemos importar métodos específicos de cada módulo
from platform import python_version, system
print(python_version())
print(system())

# usando método dir para checar todos os métodos presentes no módulo
print(dir(platform))

# chamando um método através do módulo (diretamente)
print(platform.python_version())

print('\n===========================================================')
print('MÓDULO TIME')
print('===========================================================')

""" MÓDULO TIME
Um dos módulos mais usados no Python.
Tudo que diz respeito a data, a marcar quanto tempo leva alguma ação, ou a tempo mesmo, o módulo time vai ajudar a gente

    - Marco Zero (chamado de EPOCH) = 1 de Janeiro de 1970 às 00:00:00
    - time() retorna quantos segundos se passaram desde a EPOCH
"""
import time

segundos_hoje = time.time()
print(f'Segundos desde o Marco Zero: {segundos_hoje}')

# ctime() retorna a data em string o texto no formato UTC (um formato padrão de datas)
data_hoje = time.ctime()  # ou entao data_hoje = time.ctime(time())
print(f'Data de hoje: {data_hoje}')

# verificando quantos seguindos um pedaço de código demora a rodar
tempo_inicial = time.time()
for i in range(100000000):
    pass
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print('O programa levou {} segundos para rodar'.format(duracao))

# fazer o código esperar alguns segundos (muito útil quando temos que esperar um programa ou uma página carregar)
# para esperar 5 segundos fazemos:
print('Começando')
time.sleep(5)
print('Rodou 5 segundos após')

# pegar informações de dias, hora, segundo, minuto, tudo detalhado:
# gmtime()
# gmtime().parâmetro
data_atual = time.gmtime()
print(f'Data atual: {data_atual}')

# É um objeto diferente, mas podemos pegar os parâmetros de ano, mês, dia, etc fazendo:
ano = data_atual.tm_year
mes = data_atual.tm_mon
dia = data_atual.tm_mday
hora = data_atual.tm_hour
dia_da_semana = data_atual.tm_wday

print('Hoje é dia {}/{}/{}'.format(dia, mes, ano))
