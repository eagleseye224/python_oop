class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  # Placeholder method, to be overridden by subclasses


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


# Usage
dog = Dog("Buddy")
print(dog.name)            # Output: Buddy
print(dog.species)         # Output: Dog
print(dog.make_sound())    # Output: Woof!

cat = Cat("Whiskers")
print(cat.name)            # Output: Whiskers
print(cat.species)         # Output: Cat
print(cat.make_sound())    # Output: Meow!