from datetime import datetime
import pytz  # auxilia com o fuso horário (time-zone)


# Elaborando uma classe para simular criação de conta corrente com algumas ações
class ContaCorrente:
    """  Docstring da classe: (PEP257 - padão de convenções de docstring do Python - global)

    O que faz: Cria um objeto conta corrente para gerenciar as contas dos clientes

    Atributos:
        nome (str) = nome do cliente
        cpf (str) = cpf do cliente
        saldo (float) = saldo atual da conta
        limite (float) = limite permitido do cheque especial
        transacoes (list) = armazena o histórico de transações do cliente
    """

    # definindo um método estático para fornecer informações de data e hora, não irá utilizar informações da classe
    # também é auxiliar por não fazer sentido usar fora da classe, também não precisa do self
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')  # fuso horário de BSB
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')  # método para formatar melhor as datas

    def __init__(self, nome, cpf, agencia, conta):  # quando for criada uma instância, deve-se passar todos os parâmetros
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None  # None é uma forma alternativa para não se definir um valor no momento
        self.transacoes = []  # para armazenar um histórico de transações financeiras na conta

    def deposito(self, valor):
        """
        Realiza um depósito na conta do cliente, acrescentando seu respectivo saldo
        :param valor: Valor a ser depositado na conta
        :return: None
        """
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora(), self.nome))

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
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora(), self.nome))

    def mostrar_saldo(self):
        print(f"Saldo em conta: R$ {self.saldo:,.2f}")

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite do cheque especial é de R$ {self.limite:.2f}')

    def consultar_transacoes(self):
        print(f'\nHistórico de transações: {self.nome}')
        print('Valor  |  Saldo  |  Data e hora')
        for transacao in self.transacoes:
            print(transacao)

    # método que usa como parâmetro um outro objeto/instância da classe
    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora(), conta_destino.nome))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora(), self.nome))


""" O método 'limite_conta' é um método auxiliar, ou seja, usado por outro método dentro da mesma classe, apenas dentro
da classe (não será chamado diretamente no programa). há uma convenção que informa aos programadores que irão utilizar a
classe de colocar um único underline na frente do nome do método, caracterizando-o como privado, interno da classe.
trata-se de uma sinalização para não utilizar indevidamente """

# criando uma conta corrente
conta_Victor = ContaCorrente('Victor', '04212312312', 3672, '0001')
conta_Victor.mostrar_saldo()

# depositando dinheiro na conta
conta_Victor.deposito(10000)
conta_Victor.mostrar_saldo()

# sacando dinheiro na conta
conta_Victor.saque(11000)

# verificando as transações
conta_Victor.consultar_transacoes()

# criando uma nova conta
conta_Yasmin = ContaCorrente('Yasmin', '05512312312', 3672, '0002')
conta_Yasmin.mostrar_saldo()

conta_Victor.transferir(500, conta_Yasmin)
conta_Victor.consultar_transacoes()
conta_Yasmin.consultar_transacoes()

# verificando o docstring da classe
help(ContaCorrente)