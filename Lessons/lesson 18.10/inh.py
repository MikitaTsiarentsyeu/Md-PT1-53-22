class Animal:

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print("sleeping...")

    def eat(self, smtng):
        print(f"eating {smtng}")

class Cat(Animal):

    def play(self, smtng):
        print(f"playing with {smtng} till it's broken")

class Dog(Animal):

    def woof(self):
        print(f"WOOF MOTHERF*CKER")

c = Cat("tishka")
c.sleep()
c.eat("fish")
c.play("pencil")

d = Dog("Zephirka")
d.sleep()
d.eat("eat")
d.woof()

# d.play()