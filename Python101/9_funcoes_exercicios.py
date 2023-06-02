"""
Function para Cálculo de Carga Tributária (exemplo imaginário)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.
Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um determinado produto,
dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.

Repare que preço - custo não é igual ao lucro, porque ainda foi descontado o imposto.
Sua functiona deve calcular qual foi o % de imposto aplicado sobre o preço total.
"""

preco = 1500
custo = 400
lucro = 800


def tributo(valor_preco, valor_custo, valor_lucro):
    perc = (valor_preco - valor_custo - valor_lucro) / valor_preco
    return perc


print(f'Valor do imposto: {tributo(preco, custo, lucro):.1%}')

