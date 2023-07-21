print('\n===========================================================')
print('INTRODUÇÃO')
print('===========================================================')

msg = 'Strings examples in Python, it\'s interesting'
print(msg + msg)  # a mensagem será replicada sem espaçamento entre uma e outra
print(msg, msg)  # agora temos um espaço entre elas
print(msg*2)  # mesmo resultado acima
print(msg.upper())  # colocando tudo em maiúsculo
print(msg.lower())  # colocando tudo em minúsculo
print(msg.capitalize())  # coloca em maiúsculo somente a primeira letra da string
print(msg.title())  # coloca em maiúsculo a primeira letra de cada palavra da string
print(len(msg))  # imprime o tamanho da string
print(msg.count('python'))  # é case sensitive, retorna zero

print('\n===========================================================')
print('SLICING')
print('===========================================================')
print('Exemplos de slicing')
print(msg[5])  # imprime o caracter da 5ª posição da string
print(msg[-1])  # imprime o caracter da última posição da string
print(msg[2:7])  # imprime os caracteres entre as posições 2 (incluso) e 7 (excludente, vai até a 6)
print(msg[:10])  # # imprime os caracteres entre as posições 0 (incluso) e 10 (excludente, vai até a 9)

msg = 'welcome to Python 101: Strings'
msg1 = msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]
print(msg1.title())
print(msg1[::-1].title())  # imprime a string ao contrário

print('\n===========================================================')
print('FIND/REPLACE, FORMATAÇÃO')
print('===========================================================')

print('Exemplos de substituição e formatação\n')
msg = """Dear Terry,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""

print(msg)
print(msg.find('D'))  # retorna a posição onde o caracter 'D' está
print(msg.find('Terry'))  # retorna a posição onde a palavra 'Terry' começa
print(msg.replace('Terry', 'Victor'))  # substitui palavras/letras, porém não salva na string depois de executado
print(msg)
msg = msg.replace('Terry', 'Victor')  # agora substitui e salva na string a atualização
print(msg)

print('\n===========================================================')
print('MEMBERSHIP')
print('===========================================================')

print('Victor' in msg)  # retorna True/False se 'Victor' existe na msg1
print('Victor' not in msg)

print('\n===========================================================')
print('FSTRING')
print('===========================================================')

name = 'TERRY'
color = 'RED'
msg = '[' + name.capitalize() + '] loves the color ' + color.lower() + '!'
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# msg1 traz o mesmo resultado que a msg, porém traz mais clareza ao usar FSTRING
print(msg)
print(msg1)

print('\n===========================================================')
print('FORMATAÇÃO')
print('===========================================================')

""" Como usar o format para criar formatações personalizadas em prints e textos.

:<		Alinha o texto à esquerda (se tiver espaço na tela para isso)
:>		Alinha o texto à direita (se tiver espaço na tela para isso)
:^		Alinha o texto ao centro (se tiver espaço na tela para isso)
:+		Coloca o sinal sempre na frente do número (independente se é positivo ou negativo)
:,		Coloca a vírgula como separador de milhar
:_		Coloca o _ como separador de milhar
:e		Formato Científico
:f		Número com quantidade fixa de casas decimais
:x		Formato HEX minúscula (para cores)
:X		Formato HEX maiúscula (para cores)
:%		Formato Percentual
"""
print('\nExemplo de Alinhamento')
email = 'lira@gmail.com'
print('Meu e-mail não é {:<30}, show?'.format(email))

print('\nExemplo de Edição de Sinal')
custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

print('\nExemplo de Separador de Milhar')
custo = 500
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:+} e lucro foi {:+}'.format(faturamento, lucro))

print('\nFormato com casas Decimais fixas')
custo = 5006
faturamento = 270
lucro = faturamento - custo
print('Faturamento foi {:.2f} e lucro foi {:2f}'.format(faturamento, lucro))

print('\nFormato Percentual')
custo = 500
faturamento = 1300
lucro = faturamento - custo
margem = lucro / faturamento
print('Margem de lucro foi de {:.2%}'.format(margem))


print('\nFormato Moeda -> Combinação de Formatos')
""" Existem módulos/bibliotecas que vão facilitar isso, caso a gente queira.
Também pode ser feito por substituições em string """
custo = 5000
faturamento = 27000
lucro = faturamento - custo
print('Faturamento foi R${:,.2f} e lucro foi R${:,.2f}'.format(faturamento, lucro))

# transformando no formato brasileiro
lucro_texto = 'R${:_.2f}'.format(lucro)
print(lucro_texto.replace('.', ',').replace('_', '.'))

print('\nFunção round() para arredondar números, caso seja necessário')
imposto = 0.15758
preco = 100
valor_imposto = round(preco * imposto, 1)
print('Imposto sobre o preço é de {}'.format(valor_imposto))

""" MÉTODOS ÚTEIS PARA STRINGS

- capitalize() -> Coloca a 1ª letra Maiúscula

Uso: 
        texto = 'lira'
        print(texto.capitalize())
    Resultado: 
        'Lira'

- casefold() -> Transforma todas as letras em minúsculas (existe lower() mas o casefold é melhor normalmente)

Uso: 
        texto = 'Lira'
        print(texto.casefold())
    Resultado: 
        'lira'

- count()	-> Quantidade de vezes que um valor aparece na string

Uso:
        texto = 'lira@yahoo.com.br'
        print(texto.count('.'))
    Resultado:
        2

- endswith() -> Verifica se o texto termina com um valor específico e dá como resposta True ou False

Uso:
        texto = 'lira@gmail.com'
        print(texto.endswith('gmail.com'))
    Resultado:
        True

- find() -> Procura um texto dentro de outro texto e dá como resposta a posição do texto encontrado

Uso:
        texto = 'lira@gmail.com'
        print(texto.find('@'))
    Resultado:
        4
    Obs: lembrando como funciona a posição nas strings, então o @ está na posição 4
    l i r a @ g m a i l  .  c  o  m
    0 1 2 3 4 5 6 7 8 9 10 11 12 13

- format() -> Formata uma string de acordo com os valores passados. Já usamos bastante ao longo do programa.

Uso:
        faturamento = 1000
        print('O faturamento da loja foi de {} reais'.format(faturamento))
    Resultado:
        'O faturamento da loja foi de 1000 reais'

- isalnum() -> Verifica se um texto é todo feito com caracteres alfanuméricos (letras e números) -> letras com acento ou
                ç são considerados letras para essa função.

Uso:
        texto = 'João123'
        print(texto.isalnum())
    Resultado:
        True
    Obs: se o texto fosse 'Jo~ao' ou então 'Joao#' o resultado seria False

- isalpha() -> Verifica se um texto é todo feito de letras.

Uso:
        texto = 'João'
        print(texto.isalpha())
    Resultado:
        True
    Obs: nesse caso se o texto fosse 'Joao123' o resultado seria False, porque 123 não são letras.

- isnumeric()	-> Verifica se um texto é todo feito por números.

Uso:
        texto = '123'
        print(texto.isnumeric())
    Resultado:
        True
    Obs: existem os métodos isdigit() e isdecimal() que tem variações pontuais em caracteres especiais tipo textos com 
    frações e potências, mas para 99% dos casos eles não vão ser necessários.

- replace() -> Substitui um texto por um outro texto em uma string.

Uso:
        texto = '1000.00'
        print(texto.replace('.', ','))
    Resultado
        '1000,00'
    Obs: o replace precisa de 2 argumentos para funcionar. O 1º é o texto que você quer trocar. O 2º é o texto que você 
    quer colocar no lugar daquele texto que você está tirando.

- split()	-> Separa uma string de acordo com um delimitador em vários textos diferentes.

Uso:
        texto = 'lira@gmail.com'
        print(texto.split('@'))
    Resultado:
        ['lira', 'gmail.com']

- splitlines() -> separa um texto em vários textos de acordo com os "enters" do texto

Uso:
        texto = '''Olá, bom dia
        Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.
        Faturamento = R$2.500,00
        '''
        print(texto.splitlines())
    Resultado:
        ['Olá, bom dia', 'Venho por meio desse e-mail lhe informar o faturamento da loja no dia de hoje.', 'Faturamento 
        = R$2.500,00']

- startswith() -> Verifica se a string começa com determinado texto

Uso:
        texto = 'BEB123453'
        print(texto.startswith('BEB'))
    Resultado:
        True

- strip()	-> Retira caracteres indesejados dos textos. Por padrão, retira espaços "extras" no início e no final

Uso:
        texto = ' BEB123453 '
        print(texto.strip())
    Resultado:
        'BEB123453'

- title() -> Coloca a 1ª letra de cada palavra em maiúscula

Uso:
        texto = 'joão paulo lira'
        print(texto.title())
    Resultado:
        'João Paulo Lira'

- upper()	-> Coloca o texto todo em letra maiúscula

Uso:
        texto = 'beb12343'
        print(texto.upper())
    Resultado:
        'BEB12343'
"""