# Elaborando uma classe para simular criação de conta corrente com algumas ações
class ContaCorrente:
    def __init__(self, nome, cpf):  # quando for criada uma instância, deve-se passar todos os parâmetros
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        print(f"Saldo em conta: R$ {self.saldo:,.2f}")


# criando uma conta corrente
conta_Victor = ContaCorrente('Victor', '04295656151')
conta_Victor.mostrar_saldo()

# depositando dinheiro na conta
conta_Victor.deposito(10000)
conta_Victor.mostrar_saldo()

# sacando dinheiro na conta
conta_Victor.saque(5000)
conta_Victor.mostrar_saldo()

