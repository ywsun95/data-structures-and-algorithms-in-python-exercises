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


class AbsoluteDifferenceProgression(Progression):
    """Iterator producing a absolute difference progression."""

    def __init__(self, first=2, second=200):
        """Create a new difference progression.

        first    the first term of the progression (default 2)
        second   the second term of the progression (default 200)
        """
        super().__init__(first)              # start progression at first
        self._prev = first - second

    def _advance(self):
        """Update current value by taking difference of previous two."""
        self._prev, self._current = self._current, abs(self._prev - self._current)


class SquareRootProgression(Progression):
    """Iterator producing a square root progression."""

    def __init__(self, first=65536):
        """Create a new square root progression.

        first    the first term of the progression (default 65536)
        """
        super().__init__(first)              # start progression at first

    def _advance(self):
        """Update current value by square root previous value."""
        self._current **= 0.5


if __name__ == '__main__':
    print("2.31")
    af = AbsoluteDifferenceProgression()
    af.print_progression(10)

    print("2.32")
    sr = SquareRootProgression()
    sr.print_progression(10)