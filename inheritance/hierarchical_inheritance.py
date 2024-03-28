# Hierarchical Inheritance: more than one child class are created from a single parent class.

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


class Cat(Animal):
    def __init__(self, name):
        super().__init__('Cat')
        self.name = name

    def make_sound(self):
        return "Meow!"


# Creating instances of the classes
dog = Dog("Buddy")
print(dog.species)        # Output: Dog
print(dog.name)           # Output: Buddy
print(dog.make_sound())   # Output: Woof!

cat = Cat("Whiskers")
print(cat.species)        # Output: Cat
print(cat.name)           # Output: Whiskers
print(cat.make_sound())   # Output: Meow!

