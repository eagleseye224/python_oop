class Animal:
    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Function that demonstrates polymorphic behavior
def make_animal_sound(animal):
    return animal.make_sound()


# Creating instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the function with different objects
print(make_animal_sound(animal))  # Output: Some generic sound
print(make_animal_sound(dog))     # Output: Woof!
print(make_animal_sound(cat))     # Output: Meow!
