
class Flower:

    def __init__(self, name: str, petals: int, price: float):
        self._name = name
        self._petals = petals
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_petals(self):
        return self._petals

    def set_petals(self, petals: int):
        self._petals = petals

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price


if __name__ == '__main__':
    rose = Flower('rose', 18, 9.9)
    print('flower name:', rose.get_name())
    print('flower petals:', rose.get_petals())
    print('flower price:', rose.get_price())

    rose.set_name('white rose')
    rose.set_petals(16)
    rose.set_price(15.9)
    print('specify rose attribute.')
    print('flower name:', rose.get_name())
    print('flower petals:', rose.get_petals())
    print('flower price:', rose.get_price())
