# pyautogui - ferramenta que permite automatizar mouse, teclado e tela do computador: 'pip install pyautogui'
import pyautogui
import time  # permite controlar o tempo
import pandas  # para a parte 4 em diante
import pyperclip  # para colar textos com caracteres especiais

# Pyautogui.click -> clique com o mouse
# Pyautogui.write-> escrever um texto
# Pyautogui.press -> apertar uma tecla
# Pyautogui.hotkey -> apertar combinação de teclas (CTRL + T)

# Começar escrevendo o passo a passo do código em Português (lógica do programa)

# 1 entrar no sistema da empresa

pyautogui.PAUSE = 1  # aguarda 1 segundo entre cada comando do pyautogui, para não haver falta de sincronismo

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "t")
pyautogui.write("URL DESEJADA")
pyautogui.press("enter")

# 2 fazer login (pode ser que o navegador tenha que carregar)
time.sleep(5)  # esperar nessa linha de código 5s para dar tempo do navegador carregar

time.sleep(5)  # dando uma pausa pra pegar informação da posição do mouse
print(pyautogui.position())  # pyautogui.position - mostra a posição xy do mouse

pyautogui.click()  # passar a posição do mouse na tela
pyautogui.write("DIGITAR LOGIN")  # passar a posição do mouse na tela

pyautogui.click()  # passar a posição do mouse na tela
pyautogui.write("DIGITAR SENHA")  # passar a posição do mouse na tela

pyautogui.click()  # passar a posição do mouse na tela para o botao de acessar

# 3 exportar a base de dados

# usar o click com os parametros do mouse separados para baixar a base de dados

# 4 calcular os indicadores (instalar pandas, numpy e openpyxl)

tabela = pandas.read_csv(r"C:users... caminho do arquivo com o nome", sep=";")
# esse 'r' antes é para informar ao python exatamente como está descrito, sem interpretar contrabarras de maneira errada
# significa rawstring
# sep indica com qual caracter devem ser separadas as colunas, se necessário

print(tabela)

total_gasto = tabela["ValorFinal"].sum()  # para pegar a coluna do arquivo via pandas, usar colchetes
quantidade = tabela["Quantidade"].sum()
preco_medio = total_gasto / quantidade
print(total_gasto)
print(quantidade)
print(preco_medio)

# 5 enviar e-mail com o relatório

# entrar no e-mail
# clicar em escrever
# preencher informacoes do email (destinatario, assunto, anexos, etc)
# enviar o email

# o comando write não escreve caracteres especiais/com acento
# a solução é utilizar pyperclip:

pyperclip.copy("Relatório de vendas")
pyautogui.hotkey("ctrl", "v")

texto = f'''
Prezados,
Segue o relatório de compras:

Total gasto: R${total_gasto:, .2f}
Quantidade de produtos: {quantidade:,}
Preço médio: {preco_medio:, .2f}
'''

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")