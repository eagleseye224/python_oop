# Multilevel Inheritance: a child class inherits from its parent class, which is inheriting from its parent class.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"


class Pet(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def play(self):
        return f"{self.name} is playing"


class Dog(Pet):
    def __init__(self, name):
        super().__init__('Dog', name)


# Creating an instance of the Dog class
dog = Dog("Buddy")
print(dog.species)        # Output: Dog
print(dog.name)           # Output: Buddy
print(dog.make_sound())   # Output: Some generic sound
print(dog.play())         # Output: Buddy is playing



