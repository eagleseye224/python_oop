
# Single Inheritance: a child class inherits from only one parent class.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name):
        super().__init__('Dog')
        self.name = name

    def make_sound(self):
        return "Woof!"


# Creating instances of the classes
animal = Animal("Generic")
print(animal.species)       # Output: Generic
print(animal.make_sound())  # Output: Some generic sound

dog = Dog("Buddy")
print(dog.name)             # Output: Buddy
print(dog.species)          # Output: Dog
print(dog.make_sound())     # Output: Woof!
