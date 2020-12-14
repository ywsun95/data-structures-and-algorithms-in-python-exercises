import random


class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d_or_s):
        """Create vector of that dimension with all zero,
           or that coordinates based on sequence.
        """
        if isinstance(d_or_s, int):
            self._coords = [0] * d_or_s
        else:
            self._coords = list(d_or_s)

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):    # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))     # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates s other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other       # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):    # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))     # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return negate values of vector."""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] -= self[j]
        return result

    def __radd__(self, other):
        """Return sum of two vectors.

        support the syntax v = [5, 3, 10, -2, 1] + u
        """
        return self.__add__(other)

    def __mul__(self, item):
        """
        if item is number, return vector which coordinates is item times of the original.
        if item is vector, return the dot product of two vectors
        :param item: number or vector
        :return: vector or number
        """
        if isinstance(item, (int, float)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = item * self[j]
        else:
            if len(self) != len(item):  # relies on __len__ method
                raise ValueError("dimensions must agree")
            result = 0
            for j in range(len(self)):
                result += self[j] * item[j]
        return result

    def __rmul__(self, item):
        """Return multiple or dot product."""
        return self.__mul__(item)


if __name__ == '__main__':
    v = Vector(3)
    u = Vector(3)
    for i in range(3):
        v[i] = random.randint(-10, 10)
        u[i] = random.randint(-10, 10)
    print('vector u:', u)
    print('vector v:', v)
    print('2.9 u - v:', u - v)
    print('2.10 -v:', -v)
    print('2.11 the list provide supports to add list object to Vector object.')
    print('     Implement the __radd__ method for the Vector class.')
    print('     Result: [5, -2, 1] + u =', [5, -2, 1] + u)
    print('2.12 v * 3:', v * 3)
    print('2.13 3 * v:', 3 * v)
    print('2.14 v * u:', v * u)
    print('2.15 Vector([4, 7, 5]):', Vector([4, 7, 5]))
