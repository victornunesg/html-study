""" LISTA DE COMPRAS """

# compras = {}
#
#
# def adicionar_item():
#     item = str(input("\nNome do novo item: "))
#     qtde = int(input("Quantidade do item: "))
#     compras[item] = qtde
#     print("Item adicionado com sucesso!")
#
#
# def remover_item():
#     apagar_item = str(input("\nItem a ser removido: "))
#     qtde = int(input("Quantidade do item: "))
#     compras[apagar_item] -= qtde
#     print("Item removido com sucesso!")
#
#
# def ver_lista():
#     print("\n")
#     print(compras)
#
#
# def mostrar_menu():
#     entrada = int(input("\nLista de compras "
#               "\n 1 - Adicionar item"
#               "\n 2 - Remover item"
#               "\n 3 - Ver lista"
#               "\n 4 - Sair"
#               "\nEntre com a opção desejada: "))
#     return entrada
#
#
# controle = 0
# while controle == 0:
#     opcao = mostrar_menu()
#     if opcao == 1:
#         adicionar_item()
#     elif opcao == 2:
#         remover_item()
#     elif opcao == 3:
#         ver_lista()
#     elif opcao == 4:
#         print("\n Programa finalizado")
#         controle=1
#         exit()
#     else:
#         print("\nOpção inválida!")
#         break

""" PREVISÃO DE VENDAS """

# previsoes = {}
# taxas = {}
#
# while True:
#     print("\n")
#     produto = str(input("Nome do produto (ou 'sair para finalizar)': "))
#     if produto == 'sair':
#         break
#
#     while True:
#         try:
#             vendas_atual = int(input("Vendas do mês atual: "))
#             taxa = float(input("Taxa de crescimento (%): "))
#             if vendas_atual < 0 or taxa < 0:
#                 raise Exception
#         except:
#             print("Entrada inválida. Por favor, digite um número válido para vendas e taxa de crescimento.")
#         else:
#             break
#
#     previsoes[produto] = vendas_atual
#     taxas[produto] = 1 + (taxa/100)
#
# for produto in previsoes:
#     print(f'{produto}: Previsão de vendas do próximo mês = R$ {previsoes[produto] * taxas[produto]:.2f}')

""" RELATÓRIO DE VENDAS """

# relatorio_vendas = {}
#
#
# def solicitar_nome_vendedor():
#     nome = input("\nDigite o nome do vendedor (ou 'sair') para finalizar: ")
#     return nome
#
#
# def solicitar_vendas():
#     try:
#         total_vendas = float(input("Valor da venda (R$): "))
#     except:
#         print('Entrada inválida, por favor tente novamente!')
#     return total_vendas
#
#
# def atualizar_dados(vendedor, vendas):
#     if relatorio_vendas.get(vendedor) is None:
#         relatorio_vendas[vendedor] = {'total_vendas': vendas, 'qtde_vendas': 1}
#     else:
#         relatorio_vendas[vendedor]['total_vendas'] += vendas
#         relatorio_vendas[vendedor]['qtde_vendas'] += 1
#
#
# def print_dados():
#     for vendedor in relatorio_vendas:
#         print(f'Vendedor: {vendedor}; Total de vendas: R$ {relatorio_vendas[vendedor]["total_vendas"]:.2f};'
#               f' Média de vendas: R$ {relatorio_vendas[vendedor]["total_vendas"] / relatorio_vendas[vendedor]["qtde_vendas"]:.2f}')
#
#
# while True:
#     nome_vendedor = solicitar_nome_vendedor()
#     if nome_vendedor == 'sair':
#         break
#     total_vendas = solicitar_vendas()
#     atualizar_dados(nome_vendedor, total_vendas)
#
# print_dados()

""" SEGMENTAÇÃO DE CLIENTES """

clientes = {}
categorias = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]

while True:
    novo_cliente = str(input("\nDigite o nome do cliente (ou 'sair' para sair): "))
    if novo_cliente.lower() == 'sair':
        break
    try:
        total_compras = float(input("Valor total das compras (R$): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para compras.")
        continue

    for item in categorias:
        valor, categoria = item
        if total_compras <= 1000:
            segmento = categoria
        elif 1000 < total_compras <= 5000:
            categoria = 'Prata'
        else:
            categoria = 'Ouro'

    clientes[novo_cliente] = categoria

print(clientes)
for cliente, categoria in clientes.items():
    print(f'Cliente: {cliente} / Categoria: {categoria}')

