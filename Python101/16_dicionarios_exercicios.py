"""
It’s...not really an adventure game...#Ver 1.0
Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to
save your village, and probably some good-looking girl or boy you want to marry. All prices in gold pieces excl. VAT
The code should allow you to get 1 thing from each store and each item you get should be removed from the store
inventory, then do same for next store...
one way to buy by typing the key 'newt' in an input box...or something
at end you should print the 'items' you have taken, in this version you don't have to pay for stuff or add it up

ver 1.2 add ability to exit a store without buying and go to next by typing 'exit',
and to exit if a nonexistent item is bought(typed)
Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about
total cost and how much gold you have left

ver 1.4 random bug fix, ' browser compatibility', refactoring code... basically being lazy ..stop scrolling TikTok

Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all
stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management..
as in all games there is a special way to do this that actually makes money and solves the problem...
can you find 'them'? Do you know why? May require knowledge of actual python 'lore'
"""
# # create stores
# freelancers = {
#     'name': 'freelancing Shop', 'brian': 70, 'black knight': 20,
#     'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15}
#
# antiques = {'name': 'Antique Shop', 'french castle': 400,
#             'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5}
#
# pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}
#
# # creating an empty dict to represent the cart
# cart = {}
#
# # creating a purse to represent a credit to be used in the shopping
# purse = 1000
#
# # this string will be used to inform the name and value of an item that has been bought
# bought_items = ''
#
# # creating a dict containing all the stores inventory to inform how it is before the selling
# department_store = {}
# for department in (freelancers, antiques, pet_shop):
#     department_store.update(department)
# department_store.pop('name')
# print('Morning inventory of stores:')
# print(sorted(department_store.items()))
# print('-----------------')
#
# # shopping begins, now we run through the shops, one by one
# for shop in (freelancers, antiques, pet_shop):
#     print('')
#     print(f'Welcome to {shop["name"]}! These are the available items: ')
#     print(f'{shop.keys()}'.lower())  # printing all shop items, in lowercase
#     print('')
#     buy_item = input('Enter the item to be bought or "exit" to go to the next shop: ')
#
#     # if user type other thing will be moved to the next loop/shop
#     if buy_item not in shop or buy_item == 'exit':
#         continue  # moves to the next loop/interaction
#
#     # updating the items bought adding the name and the value
#     bought_items = bought_items + f'{buy_item}: {shop[buy_item]} Gp '
#
#     # updating the dict cart, adding the bought item via pop statement
#     # which means that the item will be popped from the store
#     cart.update({buy_item: shop.pop(buy_item)})
#
#     # bought_items = ", ".join(list(cart.keys()))  # creating a new variable to represent all the items bought
#     # in this case we are turning the dictionary into a list first, then joining the list to get a string for better
#     # representation to the user
#
# # is important to mention that using pop will remove all the item from the shop, including its value
# # by this way we don`t have a value reduction, it removes key and value from the original dict
#
# print(cart)
# total_cost = sum(cart.values())  # calculating the total amount
# balance = purse - total_cost  # calculating the remaining balance
# print('')
# print(f'Congratulations, you`ve just bought: {bought_items}')  # here we are just printing the string of items bought
# print(f'Total cost: {total_cost} Gp / Balance: {balance} Gp')  # informing user the shopping details
#
# # creating a dict containing all the stores inventory to inform how it is after the selling
# department_store_after = {**freelancers, **antiques, **pet_shop}  # pyth 3.5
# department_store_after.pop('name')
# print('-----------------')
# print('Evening inventory of stores', sorted(department_store_after.items()))

"""
1. Qual foi o item mais vendido nas categorias 'livros' e 'lazer'?
2. Quanto foi vendido de 'notebook asus' e de 'ipad'?
3. Quais produtos venderam mais de 5000 unidades?
"""
mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista',
                 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720,
                     'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000,
                     'notebook asus': 2450}

# Resposta do item 1
livro = mais_vendidos['livros']
lazer = mais_vendidos['lazer']
print(f'Livro mais vendido: {livro}')
print(f'Lazer mais vendido: {lazer}')

# Resposta do item 2 - Usando o método GET
notebook = vendas_tecnologia.get('notebook asus')
ipad = vendas_tecnologia.get('ipad')
print(f'Vendas de Notebook Asus: {notebook} unidades')
print(f'Vendas de iPad: {ipad} unidades')

# Resposta do item 3 - Usando o método ITEMS dentro de um FOR (UNPACKING)
for produto, unidades in vendas_tecnologia.items():
    if vendas_tecnologia[produto] > 5000:
        print(f'Produto: {produto}. Vendas: {unidades} unidades vendidas.')

""" 1. Identificando Locais de Risco

Digamos que você está construindo um programa para identificar níveis de CO2 (gás carbônico) em determinados locais para
evitar potenciais acidentes. Em cada um desses locais a sua empresa tem 5 sensores que captam o nível de CO2 do local.

Os níveis normais de CO2 são em média 350. O nível de CO2 de um local é dado pela média captada pelos 5 sensores.

Isso significa que se tivermos os 5 sensores do Rio de Janeiro marcando: 350, 400, 450, 350, 300, o nível de CO2 do Rio
de Janeiro será dado por: (350 + 400 + 450 + 350 + 300) / 5 = 370.

Caso o nível seja maior do que 450, um aviso deve ser exibido pelo seu programa dizendo, por exemplo: Rio de Janeiro
está com níveis altíssimos de CO2 (490), chamar equipe especializada para verificar a região.

Os resultados dos sensores são monitorados frequentemente e são dados para o sistema em forma de dicionário:"""

# niveis_co2 = {
#     'AC': [325, 405, 429, 486, 402],
#     'AL': [492, 495, 310, 407, 388],
#     'AP': [507, 503, 368, 338, 400],
#     'AM': [429, 456, 352, 377, 363],
#     'BA': [321, 508, 372, 490, 412],
#     'CE': [424, 328, 425, 516, 480],
#     'ES': [449, 506, 461, 337, 336],
#     'GO': [425, 460, 385, 485, 460],
#     'MA': [361, 310, 344, 425, 490],
#     'MT': [358, 402, 425, 386, 379],
#     'MS': [324, 357, 441, 405, 427],
#     'MG': [345, 367, 391, 427, 516],
#     'PA': [479, 514, 392, 493, 329],
#     'PB': [418, 499, 317, 302, 476],
#     'PR': [420, 508, 419, 396, 327],
#     'PE': [404, 444, 495, 320, 343],
#     'PI': [513, 513, 304, 377, 475],
#     'RJ': [502, 481, 492, 502, 506],
#     'RN': [446, 437, 519, 356, 317],
#     'RS': [427, 518, 459, 317, 321],
#     'RO': [517, 466, 512, 326, 458],
#     'RR': [466, 495, 469, 495, 310],
#     'SC': [495, 436, 382, 483, 479],
#     'SP': [495, 407, 362, 389, 317],
#     'SE': [508, 351, 334, 389, 418],
#     'TO': [339, 490, 304, 488, 419],
#     'DF': [376, 516, 320, 310, 518],
# }
#
# # Opção 1 - usando o FOR 'simples'
# for estado in niveis_co2:
#     media = sum(niveis_co2[estado]) / len(niveis_co2[estado])
#     if media > 450:
#         print(f'{estado} está com níveis altíssimos de CO2 ({niveis_co2[estado]}),'
#               f' chamar equipe especializada para verificar a região.')
#
# # Opção 2 - usando o método .items() com o FOR
# for chave, valor in niveis_co2.items():
#     media = sum(valor) / len(valor)
#     # print(chave, media)
#     if media > 450:
#         print(f'{chave} está com níveis altíssimos de CO2 ({media}),'
#               f' chamar equipe especializada para verificar a região.')

""" 2. Case da Hashtag

Recentemente tivemos que fazer backup dos vídeos que temos hospedados no Vimeo. Acontece que não existe um botão de
Download de todos os vídeos ao mesmo tempo, precisamos entrar em 1 por 1 e fazer o download manualmente.

A alternativa é gerar um código em Python que converse com a API do Vimeo (API é uma integração que as ferramentas abrem
para programadores poderem fazer integrações dos seus próprios programas/scripts com a ferramenta).

Para resolver isso, a gente fez a integração e fizemos uma "requisição" de todos os vídeos para a Vimeo. Essa requisição
dá como resposta para o nosso código o relatado logo abaixo.

Repare que é um código completamente confuso, mas que no fim do dia é um dicionário.
Dentro dele queremos printar o link de download do vídeo para depois simplesmente clicar em todos os links e fazer o
download de todos os vídeos.

No nosso caso, tínhamos uma lista com os mais de 2.000 vídeos (sendo cada vídeo um dicionário exatamente como esse aí em
cima), e por isso fizemos exatamente esse mesmo procedimento que você vai construir aqui abaixo, só que dentro de um
"for" para percorrer todos os vídeos. Não podemos disponibilizar a lista inteira por questões de segurança e proteção de
dados mesmo, mas o dicionário acima já vale o exemplo. """

# video = {'uri': '/videos/465407533',
#          'name': '15 Atalhos no Excel para Ficar Mais Produtivo',
#          'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080,
#                        'expires': '2020-10-07T04:00:55+00:00',
#                        'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d'
#                                '481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5C'
#                                'VideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2B'
#                                'Mais%2BProdutivosource.mp4',
#                        'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442,
#                        'md5': 'af09508ceceed4994554f04e8b931e22',
#                        'public_name': 'Original', 'size_short': '384.02MB'},
#                       {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080,
#                        'expires': '2020-10-07T04:00:55+00:00',
#                        'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032'
#                                '396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5C'
#                                'VideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2B'
#                                'Mais%2BProdutivo175.mp4',
#                        'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205,
#                        'md5': '3c05e1e69bd6b13eb1464451033907d2',
#                        'public_name': 'HD 1080p', 'size_short': '165.52MB'},
#                       {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540,
#                        'expires': '2020-10-07T04:00:55+00:00',
#                        'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b'
#                                '30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5C'
#                                'VideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2B'
#                                'Mais%2BProdutivo165.mp4',
#                        'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848,
#                        'md5': '4a5c5c96cdf18202ed20ca534fd88007',
#                        'public_name': 'SD 540p', 'size_short': '85.72MB'},
#                       {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240,
#                        'expires': '2020-10-07T04:00:55+00:00',
#                        'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc9'
#                                '49d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5C'
#                                'VideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2B'
#                                'Mais%2BProdutivo139.mp4',
#                        'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450,
#                        'md5': '91cc0229087ec94bf67f64b01ad8768d',
#                        'public_name': 'SD 240p', 'size_short': '26.13MB'},
#                       {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360,
#                        'expires': '2020-10-07T04:00:55+00:00',
#                        'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154'
#                                'ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5C'
#                                'VideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2B'
#                                'Mais%2BProdutivo164.mp4',
#                        'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155,
#                        'md5': '548640bf79ce1552a3401726bb0e4224',
#                        'public_name': 'SD 360p', 'size_short': '46.37MB'}]}
#
#
# print(f'video: {type(video)}')  # Video é um dicionário
# print(f"video['download']: {type(video['download'])}")  # A chave "downloads' tem como valor uma lista
# print(f"video['download'][0]: {type(video['download'][0])}")  # Cada item dessa lista é um dicionário
#
# # Acessando o primeiro dicionário da lista de downloads, do type = source
# print(video['download'][0])
#
# # Como queremos printar o link da source, então basta acessarmos a chave 'link' dentro desse dicionário
# print(video['download'][0]['link'])
