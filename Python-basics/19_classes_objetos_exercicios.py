from datetime import datetime
from random import randint  # para gerar os numeros dos cartões
import pytz  # auxilia com o fuso horário (time-zone)


# BLOCO DA DEFINIÇÃO DE CLASSES


# Definindo uma classe para simular criação de conta corrente com algumas ações
class ContaCorrente:
    """  Exemplo de Docstring da classe: (PEP257 - padão de convenções de docstring do Python - global)

    O que faz: Cria um objeto conta corrente para gerenciar as contas dos clientes

    Atributos:
        nome (str) = nome do cliente
        cpf (str) = cpf do cliente, deve ser inserido com pontos e traços
        saldo (float) = saldo atual da conta do cliente
        agencia (int) = agência responsável pela conta do cliente
        conta (str) = numero da conta corrente do cliente, deve ser colocados os digitos verificadores com traco
        limite (float) = limite permitido do cheque especial
        transacoes (list) = armazena o histórico de transações do cliente
    """

    # definindo um método estático para fornecer informações de data e hora, não irá utilizar informações da classe
    # também é auxiliar por não fazer sentido usar fora da classe, não precisa do self por não usar atributos da Classe
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')  # fuso horário de BSB
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')  # método para formatar melhor as datas

    def __init__(self, nome, cpf, agencia, conta):  # quando for instanciada, deve-se passar todos os parâmetros
        self.nome = nome
        self._cpf = cpf  # atributos não públicos
        self._saldo = 0
        self._agencia = agencia
        self._conta = conta
        self._limite = None  # None é uma forma alternativa para não se definir um valor no momento
        self._transacoes = []  # para armazenar um histórico de transações financeiras na conta
        self.cartoes = []  # cartões de crédito vinculados à conta, público pois é acessado por outra classe

    def deposito(self, valor):
        """ exemplo de docstring do método, para ter descrição quando utilizado o comando help(Classe)

        Realiza um depósito na conta do cliente, acrescentando seu respectivo saldo
        :param valor: Valor a ser depositado na conta
        :return: None
        """
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora(), self.nome))

    # criando um método auxiliar (underline antes do nome), não será utilizado no bloco do programa, apenas interno
    def _limite_conta(self):
        self._limite = -1000  # definindo o limite do cheque especial
        return self._limite  # retornando o atributo após definir seu valor

    def saque(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Você não pode realizar o saque, pois não há saldo disponível em conta')
            self.mostrar_saldo()
        else:
            self._saldo -= valor
            self.mostrar_saldo()
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora(), self.nome))

    def mostrar_saldo(self):
        print(f"Saldo em conta: R$ {self._saldo:,.2f}")

    def consultar_limite_chequeespecial(self):
        print(f'Seu limite do cheque especial é de R$ {self._limite:.2f}')

    def consultar_transacoes(self):
        print(f'\nHistórico de transações: {self.nome}')
        print('Valor  |  Saldo  |  Data e hora')
        for transacao in self._transacoes:
            print(transacao)

    # método que usa como parâmetro um outro objeto/instância da classe
    def transferir(self, valor, conta_destino):
        """
        :param valor: valor a ser transferido entre contas
        :type conta_destino: ContaCorrente
        """
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora(), conta_destino.nome))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora(), self.nome))


# Definindo uma classe de cartão de crédito, para exemplificar a relação entre classes
class CartaoCredito:

    @staticmethod  # reutilizando o método para determinar a validade do cartão
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')  # fuso horário de BSB
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        """

        :rtype: CartaoCredito
        """
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000  # padrão, pode ser alterado por método
        self._senha = '1234'  # padrão, pode ser alterado por simples atribuição
        self.conta_corrente = conta_corrente
        # abaixo estamos criando a relação entre as classes CartaoCredito e ContaCorrente
        conta_corrente.cartoes.append(self)  # adicionando o objeto cartão de crédito à conta corrente

    # definindo getter e setter para realizar validação de senha caso seja alterada por atribuição no programa
    @property
    def senha(self):  # o nome do método deve ser o nome do atributo sem o underline para facilitar o acesso
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        if nova_senha == 4 and nova_senha.isnumeric():
            self._senha = nova_senha
        else:
            print('Senha inválida')


"""BLOCO DO PROGRAMA"""
# criando uma conta corrente
print('Conta corrente do Victor criada')
conta_Victor = ContaCorrente('Victor', '04212312312', 3672, '0001')
conta_Victor.mostrar_saldo()


# depositando dinheiro na conta
print('\nDepósito feito na conta corrente do Victor')
conta_Victor.deposito(10000)
conta_Victor.mostrar_saldo()


# sacando dinheiro na conta
print('\nSaque realizado na conta corrente do Victor')
conta_Victor.saque(11000)


# verificando as transações
conta_Victor.consultar_transacoes()

# criando uma nova conta
print('\nConta corrente da Yasmin criada')
conta_Yasmin = ContaCorrente('Yasmin', '05512312312', 3672, '0002')
conta_Yasmin.mostrar_saldo()


# realizando transferência
print('\nTransferência entre contas de Victor e Yasmin')
conta_Victor.transferir(500, conta_Yasmin)
conta_Victor.consultar_transacoes()
conta_Yasmin.consultar_transacoes()

# verificando o docstring da classe
print('\nDocstring da classe ContaCorrente')
print('=====================================')
help(ContaCorrente)
print('=====================================')

# criando um cartão de crédito, passando a instância da conta corrente como parâmetro
print('\nCartão de crédito do Victor criado')
cartao_Victor = CartaoCredito('Victor', conta_Victor)
print(f'Conta nº: {cartao_Victor.conta_corrente._conta}')  # acessando o nº da conta através do objeto recebido da conta
print(f'Cartão nº: {cartao_Victor.numero}')

# imprimindo dados do cartão de crédito, que foi passado como objeto para a lista de cartões na Conta Corrente
print('\nImprimindo dados gerais')
print(f'conta_Victor.cartoes: {conta_Victor.cartoes}')  # temos uma lista contendo 1 objeto
print(f'conta_Victor.cartoes[0]: {conta_Victor.cartoes[0]}')  # acessando o objeto / primeiro elemento da lista
print(f'conta_Victor.cartoes[0].numero: {conta_Victor.cartoes[0].numero}')  # acessando um atributo do objeto cartao
print(f'cartao_Victor.validade: {cartao_Victor.validade}')
print(f'cartao_Victor.cod_seguranca: {cartao_Victor.cod_seguranca}')

# tentando alterar a senha por simples atribuição
print('\nAlterando a senha do cartão para 123')
cartao_Victor.senha = '123'
print(f'Senha atual do cartão: {cartao_Victor.senha}')
