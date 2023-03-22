# ----------------------------
# CLASSES AND OBJECTS
# ----------------------------

print("\nClasses & Objects")


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
