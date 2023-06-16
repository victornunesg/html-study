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
    - etc. """

# Classes are blueprints
# Objects are the actual things you built
# variables => attributes
# functions => methods

# we use capitalization when creating classes
class Movie:
    # initialization function
    # self works referring always to the object that is active at the moment
    def __init__(self, title, year, imdb_score, have_seen):
        # self refers to the object that we are creating (convention)
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.have_seen = have_seen

    # creating a method (function) inside the class to give more details about its objects
    def nice_print(self):
        print("\nTitle: ", self.title)
        print("Year of production: ", self.year)
        print("IMDB Score: ", self.imdb_score)
        print("I have seen it: ", self.have_seen)


# creating two new object from class Movie
film_1 = Movie("Life of Brian", 1979, 8.1, True)
film_2 = Movie("The Holy Grail", 1975, 8.2, True)

# printing some attributes of film_1
print('\n', film_1.title, film_1.imdb_score)

# calling the method 'nice_print()' for film 2 in equivalent manners
film_2.nice_print()
Movie.nice_print(film_2)

# creating a list (database) with the 2 films information
films = [film_1, film_2]

# we can access the object attributes inside the list
print(films[1].title, films[0].title)

# we also can access and call the object methods inside the list
films[0].nice_print()

# ----------------------------
# CLASS INHERITANCE
# ----------------------------

# Happens when you have a class and another class which will inheritance attributes and methods from the first one
print('\nclass Inheritance')


class Person:
    def move(self):
        print('Moves 4 paces')

    def rest(self):
        print('Gains 4 health points')


# creating a new class named 'character1' which inherit class Person()
print('\nPerson')
character1 = Person()
character1.move()


# Doctor does all the things a Person does and also heals
class Doctor(Person):  # inherits from Person
    # pass  # if we put pass only, it will be identical to Person Class
    def heal(self):
        print('Heals 10 health points')


# now creating a doctor
print('\nDoctor')
character2 = Doctor()
character2.move()  # moves like Person
character2.heal()  # heals like Doctor


# Fighter overwrite move method
class Fighter(Person):
    def fight(self):
        print('Do 10 health points of damage')

    def move(self):
        print('Moves 6 paces')


print('\nFighter')
character3 = Fighter()
character3.fight()
character3.move()  # now he moves faster than a Person


# Wizard inherits 2 classes
class Wizard(Doctor, Fighter):
    def cast_spell(self):
        print('Turns invisible')

    def heal(self):
        print('Heals 15 points')


print('\nWizard')
character4 = Wizard()
character4.fight()
character4.move()
character4.heal()