import sys
import random
from time import sleep


class Animal:
    def __init__(self):
        self._gender = random.randint(0, 1)
        self._strength = random.randint(1, 10)
    
    def get_gender(self):
        """Return gender of the animal.
        
        0 resperent female, 1 resperent male
        """
        return self._gender
    
    def get_strength(self):
        """Return strength of the animal."""
        return self._strength

    def create(self):
        """Create a baby animal."""
        return self.__class__()

    def __eq__(self, other):
        return type(self) == type(other)


class Bear(Animal):
    """Bear"""
    level = 2

    def __repr__(self):
        return "B"


class Fish(Animal):
    """Fish"""
    level = 1

    def __repr__(self):
        return "F"


class Ecosystem:
    def __init__(self):
        self._river = [None] * 50
    
    def __repr__(self):
        return ' '.join([str(a) if a else '-' for a in self._river])

    def add(self, animal):
        """Add a animal to the ecosystem."""
        if None not in self._river:
            sys.exit("The ecosystem is overloaded.")
        while True:
            position = random.randint(0, len(self._river)-1)
            if self._river[position] is None:
                self._river[position] = animal
                break

    def move(self):
        """Based on a random process, each animal either attempts to move
           into an adjacent list location or stay where it is.
        """
        move_step = {}
        for pos in range(len(self._river)):
            if self._river[pos] is None:
                continue
            step = random.randint(-1, 1)
            move_step[pos] = step
        for pos, step in move_step.items():
            if 0 <= pos+step < len(self._river):
                self.collide(pos, pos+step)


    def collide(self, cur, aft):
        """two animal collide in the same cell
        
        cur    current position of animal
        aft    position after moving of animal
        """
        cur_a = self._river[cur]
        aft_a = self._river[aft]
        if cur == aft:
            pass
        elif aft_a is None:
            self._river[cur], self._river[aft] = aft_a, cur_a
        elif cur_a == aft_a:
            if cur_a.get_gender() == aft_a.get_gender():
                if cur_a.get_strength() > aft_a.get_strength():
                    self._river[cur], self._river[aft] = None, cur_a
                elif cur_a.get_strength() < aft_a.get_strength():
                    self._river[cur] = None
            else:
                baby = aft_a.create() if cur_a.get_gender() else cur_a.create()
                self.add(baby)
        else:
            if cur_a.level > aft_a.level:
                self._river[cur], self._river[aft] = None, cur_a
            else:
                self._river[cur] = None


if __name__ == "__main__":
    fauna = [Fish() for _ in range(20)] + [Bear() for _ in range(4)]
    eco = Ecosystem()
    for a in fauna:
        eco.add(a)
    for i in range(100):
        print(eco)
        eco.move()
