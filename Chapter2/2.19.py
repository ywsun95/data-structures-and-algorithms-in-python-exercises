import math


class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """

    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """Update self._current to a new value.

        This should be overridden by a subclass to customize progression.

        By convention, if current is set to None, this designates the
        end of a finite progression
        """
        self._current += 1

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:    # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current   # record current value to return
            self._advance()          # advance to prepare for next time
            return answer            # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):  # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.

        increment   the fixed constant to add to each term (default 1)
        start       the first term od the progression (default 0)
        """
        super().__init__(start)            # initialize base class
        self._increment = increment

    def _advance(self):                    # override inherited version
        """Update current value by adding the fixed increment."""
        self._current += self._increment


if __name__ == '__main__':
    print("In the arithmetic progression, the nth term of the sequence:")
    print("    an = a0 + (n - 1)d")
    print("so n = (an -a0)/d + 1")
    print("the numbers of calling next: math.ceil(2**(63-7) + 1) =", math.ceil(2**(63-7) + 1))
    print("ceil(x) return the smallest integer >= x.\n")
    ap = ArithmeticProgression(128)
    count = 1
    while next(ap) < 2**20:
        count += 1
    print('test；')
    print('the 2**63 is too large, use 2**20')
    print('in theory： math.ceil(2**(20-7) + 1) =', math.ceil(2**(20-7) + 1))
    print('in fact:', count)
