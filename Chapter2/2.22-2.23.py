from abc import ABCMeta, abstractmethod              # need these definitions


class Sequence(metaclass=ABCMeta):
    """Our own version of collection. Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:                       # found match
                return True
        return False

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:                       # leftmost match
                return j
        raise ValueError('Value not in sequence')    # never found a match

    def count(self, val):
        """"Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:                       # found a match
                k += 1
        return k

    def __str__(self):
        """Produce string of sequence."""
        return '[' + ', '.join([str(i) for i in self]) + ']'

    def __eq__(self, other):
        """Return True if two sequence have same element."""
        if len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def __lt__(self, other):
        """Return True if self sequence is less than that another sequence by lexicographic comparison."""
        for i in range(len(self)):
            if ord(str(self[i])) < ord(str(other[i])):
                return True
        return False


class ListSequence(Sequence):
    """Our own version of list."""

    def __init__(self, seq):
        """"""
        self._seq = seq

    def __len__(self):
        return len(self._seq)

    def __getitem__(self, j):
        return self._seq[j]


if __name__ == '__main__':
    s1 = ListSequence([1, 3, 6])
    s2 = ListSequence([1, 3, 6])
    s3 = ListSequence(['a', 8, 1])

    print("list s1:", s1)
    print("list s2:", s2)
    print("list s3:", s3)

    print('s1 == s2: ', s1 == s2)
    print('s1 == s3: ', s1 == s3)
    print('s1 < s2: ', s1 < s2)
    print('s1 < s3: ', s1 < s3)