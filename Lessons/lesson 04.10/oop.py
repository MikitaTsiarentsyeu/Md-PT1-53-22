class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

    def get_power(self):
        return self.__power

    def get_volume(self):
        return self.__volume

    def set_power(self, power):
        self.__power = power

    def set_volume(self, volume):
        self.__volume = volume

    power = property(get_power, set_power)
    volume = property(get_volume, set_volume)

# aggregation
class SerialCar:

    def __init__(self, make, model, color, engine):
        self.__make = make
        self.__model = model
        self.color = color
        self.engine = engine

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_engine(self, engine):
        self.__engine = engine

    def get_engine(self):
        return self.__engine

    make = property(get_make)
    model = property(get_model)
    color = property(get_color, set_color)
    engine = property(get_engine, set_engine)

# composition
class SuperCar:

    def __init__(self, make, model, color, power, volume):
        self.__make = make
        self.__model = model
        self.color = color
        self.__engine = Engine(power, volume)

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    # def set_engine(self, engine):
    #     self.__engine = engine

    # def get_engine(self):
    #     return self.__engine

    def get_power(self):
        return self.__engine.power

    def get_volume(self):
        return self.__engine.volume

    make = property(get_make)
    model = property(get_model)
    color = property(get_color, set_color)
    power = property(get_power)
    volume = property(get_volume)
    # engine = property(get_engine)

# e = Engine(120, 3)
# c = SerialCar("volvo", 'v60', 'black', e)
# print(c.make, c.model, c.color)
# c.set_color("red")
# c.color = "red"
# # c.model = "porsche"
# print(c.make, c.model, c.color)

# print(c.engine.power)
# print(c.engine.volume)

# c.engine = Engine(150, 5)
# print(c.engine.power)
# print(c.engine.volume)

c = SuperCar('ferrari', "la ferrari", 'red', 330, 8)
print(c.volume)