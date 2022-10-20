class Food:

    def __init__(self, name):
        self.name = name

class Meat(Food): pass

class Herbal(Food): pass

stake = Meat("stake")
grass = Herbal("grass")

class Animal:

    def eat(self, smtng):
        print(f"eating {smtng.name}")

    def phe(self):
        print("phe...")

class Carnivore(Animal):

    def eat(self, smtng):
        if isinstance(smtng, Meat):
            # super().eat(smtng)
            Animal.eat(self, smtng)
        else:
            super().phe()

class Herbivore(Animal):

    def eat(self, smtng):
        if isinstance(smtng, Herbal):
            # super().eat(smtng)
            Animal.eat(self, smtng)
        else:
            super().phe()

class Omnivore(Herbivore, Carnivore):

    def eat(self, smtng):
        if isinstance(smtng, Meat):
            Carnivore.eat(self, smtng)
        elif isinstance(smtng, Herbal):
            Herbivore.eat(self, smtng)
        else:
            super().phe()

tiger = Carnivore()
hare = Herbivore()
dog = Omnivore()

dog.eat(stake)
dog.eat(grass)

print(Omnivore.mro())
# for eater in [tiger, hare, dog]:
#     eater.eat(stake)
#     eater.eat(grass)