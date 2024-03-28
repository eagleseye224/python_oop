# Hybrid Inheritance: combines more than one form of inheritance.

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

    def make_sound(self):
        return "Woof!"


class GuardDog(Dog):
    def __init__(self, name):
        super().__init__(name)

    def guard(self):
        return f"{self.name} is guarding"


class Cat(Pet):
    def __init__(self, name):
        super().__init__('Cat', name)

    def make_sound(self):
        return "Meow!"


# Creating instances of the classes
dog = Dog("Buddy")
print(dog.species)        # Output: Dog
print(dog.name)           # Output: Buddy
print(dog.make_sound())   # Output: Woof!
print(dog.play())         # Output: Buddy is playing

cat = Cat("Whiskers")
print(cat.species)        # Output: Cat
print(cat.name)           # Output: Whiskers
print(cat.make_sound())   # Output: Meow!
print(cat.play())         # Output: Whiskers is playing

guard_dog = GuardDog("Max")
print(guard_dog.species)        # Output: Dog
print(guard_dog.name)           # Output: Max
print(guard_dog.make_sound())   # Output: Woof!
print(guard_dog.play())         # Output: Max is playing
print(guard_dog.guard())        # Output: Max is guarding




