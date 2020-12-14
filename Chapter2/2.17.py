
# class inheritance diagram
#
#          object
#        /   /    \
#     Goat  Pig   Horse
#                /     \
#            Racer   Equestrian


class Goat(object):

    def __init__(self, tail):
        self._tail = tail

    def milk(self):
        print("milk")

    def jump(self):
        print("jump")


class Pig(object):

    def __init__(self, nose):
        self._nose = nose

    def eat(self, food):
        print(f'eat {food}')

    def wallow(self):
        print('wallow')


class Horse(object):

    def __init__(self, height, color):
        self._height = height
        self._color = color

    def run(self):
        print("run")

    def jump(self):
        print('jump')


class Racer(Horse):

    def race(self):
        print('race')


class Equestrian(Horse):

    def __init__(self, height, color, weight):
        self._weight = weight
        super().__init__(height, color)

    def trot(self):
        print('trot')

    def is_trained(self):
        print('is_trained')
