print('\n===========================================================')
print('CLASSES E ORIENTAÇÃO A OBJETOS')
print('===========================================================')

""" REGRAS GERAIS:
Tudo no Python é um objeto: String é objeto / Lista é objeto / Dicionários são objetos ...
Objetos, na verdade, são Classes em Python
Cada Classe possui Métodos e Atributos

Comparação Clássica: Pense no Controle Remoto de uma Televisão.
    O Controle é um objeto
    Cada botão dele é um comando, um método.
    Cada método faz 1 ação específica
    Por trás de cada método (dentro do controle) podem acontecer milhares de coisas quando você aperta 1 botão, mas no
    fundo você tá cagando pra isso, só quer que o botão faça o que você mandou quando você clicar no botão.

Classe = Objeto
    Métodos = o que aquele objeto consegue fazer?
    Atributos = quais são as informações/propriedades desse objeto?

Classe = Pessoa
    Métodos = Andar, Pular, Correr, etc
    Atributos = Peso, Altura, QI, Profissão

Classe = String
    Métodos = Replace, Find, Capitalize, Format

Cada objeto é um tipo. Dizemos "É um objeto do tipo String, tipo Int, etc"

Em termos práticos no Python
Isso significa que todos eles tem métodos específicos, ou seja, já existe programado no Python várias coisas que você
consegue fazer com ele.

Exemplo: Strings
Quando no Python criaram a string, eles programaram lá em algum lugar que texto[i] vai te dar o caracter na posição i do
texto. Também criaram o método texto.upper() que torna toda a string em letra maiúscula. Também criaram o método
texto.casefold() que coloca tudo em letra minúscula. E assim vai para tudo que temos no Python
Em termos práticos, você já deve ter reparado que fazemos muito coisas do tipo variavel.método()
    
    - 'Produto {}: {} unidades vendidas'.format(produto, quantidade)
    - lista.append('ABC12304')
    - texto.count()
    - etc.
    
==================================
Vantagens da orientação a objetos:

- Aproveitar o código sem precisar refazer/copiar tudo
- Encapsulamento - proteção a mudanças indesejadas (o método está protegido dentro da definição da classe por exemplo)
- Herança - Instâncias de objetos tem as mesmas características, apesar de possuirem valores diferentes
- Polimorfismo - Um mesmo método pode ter várias formas em diferentes classes (ou subclasses)ex: Animais>GatosxCachorros

Classes são projetos
Objetos são as coisas reais que você construiu
variáveis => atributos
funções => métodos """

print('\n===========================================================')
print('CRIANDO A CLASSE "TV"')
print('===========================================================')

""" ESTRUTURA: class Nome_Classe(object)
método Init é automaticamente chamado quando se inicia a classe
é esse método que define o que acontece quando você cria uma instância da classe."""


# criando a classe de uma televisão, definindo as caracteristicas/atributos no método init
class TV:

    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'netflix'
        self.volume = 10

    # criando método para mudar um canal, recebe um novo parâmetro para alterar o atributo
    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

# BLOCO DO PROGRAMA


# criando objetos/instâncias da classe TV
tv_sala = TV()
tv_quarto = TV()

# alterando atributos dos objetos
tv_sala.cor = 'branca'
tv_quarto.mudar_canal('disney+')

# imprimindo os atributos após alterações
print(tv_sala.cor)
print(tv_quarto.cor)
print(tv_sala.canal)
print(tv_quarto.canal)

""" MAIS SOBRE O SELF

Sempre quando necessário acessar um atributo/método definido dentro da classe, é necessário ter 'self' como primeiro
parâmetro na definição de um método, bem como na definição dos atributos, caso contrário não será possível acessar fora
da classe.

'self.atributo' é como se fosse um nome só, se refere ao atributo da classe
"""


# também é possível definir parâmetros para o 'init' da classe, utilizado para que os atributos possam ser definidos no
# momento da criação do objeto, quando se chama a classe:
class TV2:
    def __init__(self, tamanho, volume):
        self.tamanho = tamanho
        self.volume = volume


# podemos passar os parâmetros através do nome
tv_salao = TV2(tamanho=32, volume=10)
# ou podemos passar na ordem
tv_banheiro = TV2(29, 12)

print(tv_salao.tamanho)
print(tv_banheiro.volume)

print('\n===========================================================')
print('ATRIBUTOS DE CLASSE')
print('===========================================================')

""" Todos os atributos definidos anteriormente (iniciados com 'self.atributo'), são atributos de instância
isto é, cada objeto pode ter valores de atributos distintos, pois podem ser alterados a qualquer momento.
Já os atributos de classe são únicos, terão os mesmos valores para qualquer objeto
podem ser alterados, porém isso refletirá em todos os objetos criados
normalmente alterar esse atributo de classe não é usual e nem recomendado quando se tem uma classe bem estruturada """


class TV3:

    # todos os objetos terão o atributo 'cor' e será 'preta' para todas as instâncias dessa classe
    cor = 'preta'

    def __init__(self):
        self.ligada = False
        self.tamanho = 55
        self.canal = 'netflix'
        self.volume = 10


tv_nova = TV3()
tv_nova2 = TV3()
print(tv_nova.cor)
print(tv_nova2.cor)

# alterando o atributo da classe TV3 e verificando as alterações logo a seguir
TV3.cor = 'branca'
print(tv_nova.cor)
print(tv_nova2.cor)


""" 
============================
MÉTODOS AUXILIARES
============================
São métodos criados nas classes somente para serem utilizados por outro(s) método(s) dentro da mesma classe, ou seja,
não será chamado diretamente no programa. Há uma convenção que informa aos programadores que irão utilizar a classe de 
colocar um único underline na frente do nome do método, caracterizando-o como privado, interno da classe. Trata-se de
uma sinalização para não utilizar indevidamente

============================
DICAS GERAIS/ORIENTAÇÕES/PADRONIZAÇÕES
============================
1) sempre definir o nome da classe com letra maiúscula (cada palavra da classe tb, maiúscula)
2) sempre 1 linha de espaço entre os métodos e 2 linhas de espaço no final
3) métodos devem ser curtos, para executar funções bem definidas e específicas
4) caso seja necessário criar uma outra lógica para aquele método criado, deve-se criar um método auxiliar para fazê-lo
5) todos os atributos de instância, ou seja, que mudam de acordo com cada objeto, devem estar no método __init__

============================
MODIFICANDO O INIT DE UMA CLASSE JÁ EXISTENTE
============================
Quando for realizar edições em uma classe, é necessário verificar impactos nos objetos/instâncias já existentes, pois
existem edições que vão exigir reestruturação do programa, como por exemplo, se alterar o init de uma classe existente
adicionando atributos novos (haverá quebras em objetos já existentes os quais não foram definidos com os atributos que
foram alterados/incluidos), mas também há edições que não causam impacto (adição de um novo método, por exemplo).

============================
MÉTODO ESTÁTICO
============================
Métodos que não utilizam informações/atributos da própria classe, 100% auxiliar também.
São definidos antes do __init__ e sem o self (pois não usa nada da classe), como se fosse uma variável global
Além disso, temos que colocar o decorator @staticmethod antes da definição do método (ver exemplo nos exercicios), para
sinalizar que se trata de um método estático.
Para usar o método estático, deve-se usar 'nome_da_classe.método_estatico()'

============================
ATRIBUTOS NÃO PÚBLICOS
============================
Atenção: Só é recomendado em casos de atributos sensíveis para a classe, ou seja, que necessariamente não podem ser
modificados fora de métodos. Desta forma, temos que 'fechar' o atributo e definir um método para manipulá-lo.

Quando se deseja tornar um atributo modificável apenas através da utilização de métodos da classe, basta colocar um _ na
frente, logo após o 'self.' que o atributo torna-se não público, porém visivel para as instâncias.
Se colocarmos dois underlines 'self.__Atributo', as instâncias da classe não irão conseguir acessá-lo, você pode restrin
gir o uso apenas para alterações dentro dos métodos da classe, mas ficará inacessível para as instâncias dela.

============================
RELACIONAMENTO ENTRE CLASSES
============================
Não se trata de subclasses, e sim duas classes que possuem relação. Exemplo: Conta corrente <> Cartão de crédito
Exemplificado no arquivo de exercícios como funciona o relacionamento entre duas classes.

============================
MÉTODOS GETTER E SETTER (raro de encontrar na prática)
============================
Caso existam atributos não públicos os quais queira restringir a maneira de alterar seu respectivo valor sem a necessida
de de usar métodos dentro da classe para tal, deve-se definir os métodos 'getter' e 'setter' para realizar validações durante a
atribuição. Com isso, ao executar um comando de atribuição:

cartão_Victor._senha = '1324'

as validações podem ocorrer caso se defina:

@property  # esse é o getter
def nome_do_atributo(self):
    return self.nome_do_atributo

@nome_do_atributo.setter
def nome_do_atributo(self):
    # validação

============================
MÉTODO PARA LISTAR/CONSULTAR INFORMAÇÕES DE UMA CLASSE
============================
nome_instancia.__dict__ lista todos os atributos e valores da instância da classe em forma de dicionário

"""







# # we use capitalization when creating classes
# class Movie:
#     # initialization function
#     # self works referring always to the object that is active at the moment
#     def __init__(self, title, year, imdb_score, have_seen):
#         # self refers to the object that we are creating (convention)
#         self.title = title
#         self.year = year
#         self.imdb_score = imdb_score
#         self.have_seen = have_seen
#
#     # creating a method (function) inside the class to give more details about its objects
#     def nice_print(self):
#         print("\nTitle: ", self.title)
#         print("Year of production: ", self.year)
#         print("IMDB Score: ", self.imdb_score)
#         print("I have seen it: ", self.have_seen)
#
#
# # creating two new object from class Movie
# film_1 = Movie("Life of Brian", 1979, 8.1, True)
# film_2 = Movie("The Holy Grail", 1975, 8.2, True)
#
# # printing some attributes of film_1
# print('\n', film_1.title, film_1.imdb_score)
#
# # calling the method 'nice_print()' for film 2 in equivalent manners
# film_2.nice_print()
# Movie.nice_print(film_2)
#
# # creating a list (database) with the 2 films information
# films = [film_1, film_2]
#
# # we can access the object attributes inside the list
# print(films[1].title, films[0].title)
#
# # we also can access and call the object methods inside the list
# films[0].nice_print()
#
# # ----------------------------
# # CLASS INHERITANCE
# # ----------------------------
#
# # Happens when you have a class and another class which will inheritance attributes and methods from the first one
# print('\nclass Inheritance')
#
#
# class Person:
#     def move(self):
#         print('Moves 4 paces')
#
#     def rest(self):
#         print('Gains 4 health points')
#
#
# # creating a new class named 'character1' which inherit class Person()
# print('\nPerson')
# character1 = Person()
# character1.move()
#
#
# # Doctor does all the things a Person does and also heals
# class Doctor(Person):  # inherits from Person
#     # pass  # if we put pass only, it will be identical to Person Class
#     def heal(self):
#         print('Heals 10 health points')
#
#
# # now creating a doctor
# print('\nDoctor')
# character2 = Doctor()
# character2.move()  # moves like Person
# character2.heal()  # heals like Doctor
#
#
# # Fighter overwrite move method
# class Fighter(Person):
#     def fight(self):
#         print('Do 10 health points of damage')
#
#     def move(self):
#         print('Moves 6 paces')
#
#
# print('\nFighter')
# character3 = Fighter()
# character3.fight()
# character3.move()  # now he moves faster than a Person
#
#
# # Wizard inherits 2 classes
# class Wizard(Doctor, Fighter):
#     def cast_spell(self):
#         print('Turns invisible')
#
#     def heal(self):
#         print('Heals 15 points')
#
#
# print('\nWizard')
# character4 = Wizard()
# character4.fight()
# character4.move()
# character4.heal()