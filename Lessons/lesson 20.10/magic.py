class FreightTrain:

    cart_len = 100

    def __init__(self, cart_count):
        self.cart_count = cart_count

    def __str__(self) -> str:
        return f"I'm a train of {self.cart_count} carts, choo-choo!"

    def __int__(self) -> int:
        return self.cart_count

    def __len__(self):
        return self.cart_count*FreightTrain.cart_len

    def __eq__(self, other) -> bool:
        if not isinstance(other, FreightTrain):
            return False

        return self.cart_count == other.cart_count

    def __add__(self, other):
        try:
            return FreightTrain(self.cart_count+other.cart_count)
        except:
            raise TypeError('can only add FreightTrain to FreightTrain')


little_train = FreightTrain(10)  
print(little_train)
print(int(little_train))
print(len(little_train))

looooooong = FreightTrain(88)
print(little_train == looooooong)

print(FreightTrain(44)+FreightTrain(44))
print(FreightTrain(44)+FreightTrain(44)==looooooong)