def prepare():
    print("STARTING A NEW PIZZA MAKING PROCESS")
    print("preparing a base")
    print("choosing a sauce")

def add_ingridient(ingridient):
    print(f"adding {ingridient}")

def grind_cheese():
    print("grinding cheese")

def bake():
    print("baking...")

def done():
    print("boxing")
    print("slicing")
    print("DONE!")

# def make_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_double_pepperoni():
#     prepare()
#     add_ingridient("pepperoni")
#     add_ingridient("pepperoni")
#     grind_cheese()
#     bake()
#     done()

# def make_cesar():
#     prepare()
#     add_ingridient("chiken")
#     add_ingridient("pork")
#     grind_cheese()
#     bake()
#     done()

def pizza_factory(ingridients):
    def factory_method():
        prepare()
        for i in ingridients:
            add_ingridient(i)
        grind_cheese()
        bake()
        done()
    return factory_method

make_pepperoni = pizza_factory(["pepperoni"])
make_double_pepperoni =  pizza_factory(["pepperoni", "pepperoni"])
make_cesar = pizza_factory(["chiken", "pork"])

make_pepperoni()
make_double_pepperoni()
make_cesar()