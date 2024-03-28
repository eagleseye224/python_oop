# Multiple Inheritance: a child class inherits from multiple parent classes.

class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"


class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is playing"


class Dog(Animal, Pet):
    def __init__(self, name):
        Animal.__init__(self, 'Dog')  # Call Animal's constructor explicitly
        Pet.__init__(self, name)       # Call Pet's constructor explicitly


# Creating an instance of the Dog class
dog = Dog("Buddy")
print(dog.species)        # Output: Dog
print(dog.name)           # Output: Buddy
print(dog.make_sound())   # Output: Some generic sound
print(dog.play())         # Output: Buddy is playing
