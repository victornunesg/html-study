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

relatorio_vendas = {}
qtde_vendas = {}

while True:
    vendedor = input("\nDigite o nome do vendedor (ou 'sair') para finalizar: ")
    if vendedor == 'sair':
        break
    vendas = input("Número de vendas: ")
    try:
        relatorio_vendas[vendedor] = vendas
    qtde_vendas[vendedor] = qtde_vendas[vendedor] + 1

print(relatorio_vendas)
print(qtde_vendas)
