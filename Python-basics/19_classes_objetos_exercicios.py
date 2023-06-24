from datetime import datetime
from random import randint  # para gerar os numeros dos cartões
import pytz  # auxilia com o fuso horário (time-zone)

# ARQUIVO USADO PARA DEFINIR AS CLASSES


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


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa atual R$ {self.caixa}')
        else:
            print(f'O valor de caixa esta OK. Caixa atual: R$ {self.caixa}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# CRIANDO SUBCLASSES DA AGENCIA
class AgenciaHeranca(Agencia):

    pass

class AgenciaVirtual(Agencia):  # recebe a classe Agencia como parâmetro

    # chama o init da subclasse, passando os parametros da superclasse e os novos da subclasse
    def __init__(self, site, telefone, cnpj):

        # inicializando o init da superclasse também, caso contrário não teremos os atributos da superclasse do init
        super().__init__(telefone, cnpj, numero=1000)  # por padrão definimos o numero 1000 para agencias virtuais

        self.site = site  # personalizando a agencia virtual com website
        self.caixa = 1000000  # personalizando a agencia virtual com um caixa diferenciado


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000  # agencias comuns também iniciam com 1M de caixa


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000  # agencias comuns também iniciam com 10M de caixa


# O CÓDIGO ABAIXO DEVE SER USADO EM UM ARQUIVO SEPARADO, 'MAIN', PARA CHAMAR AS CLASSES CRIADAS

# BLOCO DO PROGRAMA
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

# criando uma nova agencia
print('')
agencia1 = Agencia(6133516464, 999111222333, 4568)
agencia1.caixa = 2000000
agencia1.verificar_caixa()

# agencia realizando empréstimo
print('')
agencia1.emprestar_dinheiro(1500, 342042042042, 0.02)
print(agencia1.emprestimos)

# adicionando cliente em uma agencia
print('')
agencia1.adicionar_cliente('Victor', 342042042042, 300000)
print(agencia1.clientes)

# exemplificando a herança da subclasse AgenciaHeranca (herdando atributos e métodos da classe Agencia por padrão)
print('')
agencia_heranca = AgenciaHeranca(6134556699, 444555666777, 1230)
agencia_heranca.caixa = 10000000
agencia_heranca.verificar_caixa()

# criando uma agência virtual, exibindo seu website
print('')
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 6135448899, 123456789000)
print(agencia_virtual.site)

# criando uma agência comum
print('')
agencia_comum = AgenciaComum(6154460000, 789456123000)
print(agencia_comum.caixa)

# criando uma agência premium
print('')
agencia_premium = AgenciaPremium(6132145578, 789000888000)
print(agencia_premium.caixa)
