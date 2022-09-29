class Dog:

    # __name = "good boy"
    # __breed = "shepherd"
    # __color = "black"

    def __init__(self, name, breed, color="black"):
        self.name = name
        self.breed = breed
        self.color = color
        # self.set_name(name)
        # self.set_breed(breed)
        # self.set_color(color)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 0:
            if not name[0].isupper():
                name = name.title()
            self.__name = name

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
    color = property(get_color, set_color)

    def eat(self, smtng):
        print(f"eating {smtng}")

    def sleep(self):
        print("sleeping...")

d = Dog("good boy", "shepherd")
print(d.name, d.breed, d.color)
d.name = "chappy"
d.sleep()

d1 = Dog("zephyrka", "wss", "white")
print(d1.name, d1.breed, d1.color)
d1.eat("meat")

# d1.weight = 30
# print(d1.weight)

# Dog.weight = 15
# print(d.weight)
# print(d1.weight)