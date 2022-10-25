class Animal:

    def hello(self):
        print("Hello, ny name is Peter")

class Human(Animal):

    def hello(self, name):
        print(f"Hello, my name is {name}")

class NotFlyingAnimal(Animal):

    def fly(self):
        print("I cannot fly")

class FlyingAnimal(Animal):

    def fly(self):
        print("I'm flying")

class RunningAnimal(Animal):

    def run(self):
        print("I'm running")

class SwimmingAnimal(Animal):

    def swim(self):
        print("I'm swimming")

class Cat(RunningAnimal, NotFlyingAnimal):

    def say_something(self):
        print("niya!")

    def hello(self):
        print("Hello, I'm a cat")

class Dog(RunningAnimal, NotFlyingAnimal):

    def say_something(self):
        print("bork!")

    def hello(self):
        print("Hello, I'm a dog")

class Chicken(RunningAnimal, FlyingAnimal):

    def say_something(self):
        print("pock-pock!")

    def hello(self):
        print("Hello, I'm a chicken")

class Dolphin(SwimmingAnimal, NotFlyingAnimal): pass

class Seagul(FlyingAnimal): pass

class Croc(RunningAnimal, SwimmingAnimal, NotFlyingAnimal): pass

class Duck(RunningAnimal, SwimmingAnimal, FlyingAnimal): pass


animals = [Cat(), Dog(), Chicken(), Human()]

for a in animals:
    # a.hello() error for the Human instance
    a.say_something()

animals += [Dolphin(), Seagul(), Croc(), Duck()]
for a in animals:
    a.fly()