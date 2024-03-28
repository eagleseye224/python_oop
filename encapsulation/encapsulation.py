class Car:
    def __init__(self, brand, model, color):
        self.__brand = brand    # private attribute
        self.__model = model    # private attribute
        self.__color = color    # private attribute

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color


# Creating an instance of the Car class
car = Car("Toyota", "Camry", "Blue")

# Accessing private attributes using getter methods
print("Brand:", car.get_brand())    # Output: Toyota
print("Model:", car.get_model())    # Output: Camry
print("Color:", car.get_color())    # Output: Blue

# Modifying private attributes using setter methods
car.set_brand("Honda")
car.set_model("Accord")
car.set_color("Red")

print("Brand:", car.get_brand())    # Output: Honda
print("Model:", car.get_model())    # Output: Accord
print("Color:", car.get_color())    # Output: Red
