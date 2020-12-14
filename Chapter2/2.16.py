
class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError("step cannot be 0")
        if stop is None:  # special case of range(n)
            start, stop = 0, start  # show be treated as if range(0, n)

        # calculate the effective length once
        # self._length = max(0, (stop - start + step - 1) // step)

        # new type for reserve, such as range(10, 0, -2)
        if start <= stop:
            self._length = max(0, (stop - start + step - 1) // step)
        else:
            self._length = max(0, (stop - start + step + 1) // step)

        # need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (usin standard interpretation if negative)."""
        if k < 0:
            k += len(self)  # attempt to convert negative index

        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step


if __name__ == '__main__':
    print('this formula have a small flaw, that is, the result is error when start > stop.')
    print('modify as the follow:')
    print()
    print('if start <= stop:')
    print('    self._length = max(0, (stop - start + step - 1) // step)')
    print('else:')
    print('    self._length = max(0, (stop - start + step + 1) // step)')
    print()
    print('test:')
    print("Range(2, 9, 2):", list(Range(2, 9, 2)))
    print("Range(2, 9, -2):", list(Range(2, 9, -2)))
    print("Range(7, 3, 2):", list(Range(7, 3, 2)))
    print("Range(7, 3, -2):", list(Range(7, 3, -2)))