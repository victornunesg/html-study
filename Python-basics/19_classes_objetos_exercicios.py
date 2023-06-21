# Elaborando uma classe para simular criação de conta corrente com algumas ações
class ContaCorrente:
    def __init__(self, nome, cpf):  # quando for criada uma instância, deve-se passar todos os parâmetros
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None  # None é uma forma alternativa para não se definir um valor no momento

    def deposito(self, valor):
        self.saldo += valor

    def _limite_conta(self):
        self.limite = -1000  # definindo o limite do cheque especial
        return self.limite  # retornando o atributo após definir seu valor

    def saque(self, valor):
        if self.saldo - valor < self._limite_conta():
            print('Você não pode realizar o saque, pois não há saldo disponível em conta')
            self.mostrar_saldo()
        else:
            self.saldo -= valor
            self.mostrar_saldo()

    def mostrar_saldo(self):
        print(f"Saldo em conta: R$ {self.saldo:,.2f}")

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite do cheque especial é de R$ {self.limite:.2f}')

""" O método 'limite_conta' é um método auxiliar, ou seja, usado por outro método dentro da mesma classe, apenas dentro
da classe (não será chamado diretamente no programa). há uma convenção que informa aos programadores que irão utilizar a
classe de colocar um único underline na frente do nome do método, caracterizando-o como privado, interno da classe.
trata-se de uma sinalização para não utilizar indevidamente """

# criando uma conta corrente
conta_Victor = ContaCorrente('Victor', '04295656151')
conta_Victor.mostrar_saldo()

# depositando dinheiro na conta
conta_Victor.deposito(10000)
conta_Victor.mostrar_saldo()

# sacando dinheiro na conta
conta_Victor.saque(11000)

