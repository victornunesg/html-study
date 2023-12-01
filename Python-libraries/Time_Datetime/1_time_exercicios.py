import time
import locale  # traduz para português quando usamos a função strftime()

# # EXERCICIO 1: Contagem regressiva
# for i in range(10, 0, -1):
#     print(i, end=" \t")  # parâmetro end modifica como as linhas são impressas, nesse caso imprime na mesma linha
#     time.sleep(1)
#
# print("O evento começou!")
#
# # EXERCICIO 2: Exibir a data e hora atual no formato "dia da semana, dia, mês, ano, horas e minutos
# locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8') # define a localização para português
#
# tempo_em_struct = time.localtime()
# print(tempo_em_struct)
#
# tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M", tempo_em_struct)
# print(tempo_formatado)


# EXERCICIO 3: tempo até o próximo ano
# calcula quantos dias, horas, minutos e segundos faltam até o próximo ano novo

tempo_atual = time.localtime()
tempo_ano_novo = time.mktime((2024, 1, 1, 0, 0, 0, 0, 0, 0))  # passando uma tupla ordenada, na estrutura do 'struct_time', para 01/01/2024
segundos_ano_novo = tempo_ano_novo - time.mktime(tempo_atual)
print(f'\nDiferença em segundos até o ano novo: {segundos_ano_novo}')

segundos_por_minuto = 60
print(f'Segundos em um minuto: {segundos_por_minuto}')
segundos_por_hora = 60 * 60
print(f'Segundos em uma hora: {segundos_por_hora}')
segundos_por_dia = 24 * 60 * 60
print(f'Segundos em um dia: {segundos_por_dia}')

print(divmod(7,3))  # resto da divisão de 7 por 3, resulta em uma tupla (2,1) onde 2 é o quociente e 1 é o resto
resultado, resto = divmod(7,3)  # como é uma tupla, podemos fazer o unpacking

# trazendo para o exercicio, temos:

dias, resto_segundos = divmod(segundos_ano_novo, segundos_por_dia)
horas, resto_segundos = divmod(resto_segundos, segundos_por_hora)
minutos, segundos = divmod(resto_segundos, segundos_por_minuto)
print(f'\n Faltam {dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos para o Ano Novo.')

