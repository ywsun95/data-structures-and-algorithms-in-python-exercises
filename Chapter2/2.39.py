# inheritance hierarchy:
#                               Polygon
#             |--------------------|--------------------|-----------------|
#          Triangle          Quadrilateral         RegularPolygon    PolygonWithCoordinates
#          |      |          |         |           |      |      |
#  Isosceles  Equilateral  Rectangle  Square  Pentagon  Hexagon  Octagon
#  Triangle   Triangle

import math
from abc import ABCMeta, abstractclassmethod


class Polygon(metaclass=ABCMeta):
    @abstractclassmethod
    def area(self):
        """Return the area of polygon."""

    @abstractclassmethod
    def perimeter(self):
        """Return the perimeter of polygon."""


class Triangle(Polygon):
    def __init__(self, lengths: list):
        """Create a triangle.

        lengths    list of lengths of side 0f the triangle
        """
        if sum(lengths) <= max(lengths) * 2:
            raise ValueError('The length of any side must be less than the sum of the other two sides.')
        self._lengths = lengths

    def perimeter(self):
        """Return the perimeter of triangle."""
        return sum(self._lengths)

    def area(self):
        """Return the area of the triangle.

        p = 1/2(a+b+c)
        S = sqrt(p*(p-a)*(p-b)*(p-c))
        """
        semi_perimeter = self.perimeter() / 2
        area = semi_perimeter
        for l in self._lengths:
            area *= (semi_perimeter - l)
        return float('{:.2f}'.format(area**0.5))

    def __repr__(self):
        return 'lengths=' + str(self._lengths)


class IsoscelesTriangle(Triangle):
    def __init__(self, lengths):
        """Create an isosceles triangle."""
        if len(set(lengths)) > 2:
            raise ValueError("This is not an isosceles triangle.")
        super().__init__(lengths)

    def __repr__(self):
        return 'lengths=' + str(self._lengths)


class EquilateralTriangle(Triangle):
    def __init__(self, length):
        """Create an equilateral triangle.

        length    the length of side of equilateral triangle.
        """
        super().__init__([length] * 3)

    def __repr__(self):
        return 'lengths=' + str(self._lengths)


class Quadrilateral(Polygon):
    def __init__(self, lengths, angles):
        """Create a quadrilateral.

        lengths    list of lengths of sides of quadrilateral, (e.g., [a, b, c, d])
        angles   two of the opposite angles, (e.g., [A, C])

        Notion that angle A between sides a and b, and C between sides b and c.
        """
        self._lengths = lengths
        self._angles = angles

    def perimeter(self):
        """Return the perimeter of quadrilateral."""
        return sum(self._lengths)

    def area(self):
        """Return the area of quadrilateral.

        S = 1/2*a*b*sinA + 1/2*c*d*sinC
        """
        area = self._lengths[0] * self._lengths[1] * math.sin(math.radians(self._angles[0]))
        area += self._lengths[2] * self._lengths[3] * math.sin(math.radians(self._angles[0]))
        return float('{:.2f}'.format(area * 0.5))

    def __repr__(self):
        return f'lengths={str(self._lengths)}, angles={self._angles}'


class Rectangle(Quadrilateral):
    def __init__(self, lengths):
        """create a rectangle

        lengths   include base and height of the rectangle
        """
        super().__init__(lengths*2, [90]*2)

    def __repr__(self):
        return f"base={self._lengths[0]}, height={self._lengths[1]}"


class Square(Quadrilateral):
    def __init__(self, length):
        """Create a Square.

        length     the length of side of the square.
        """
        super().__init__([length]*4, [90]*2)

    def __repr__(self):
        return f'length={self._lengths[0]}'


class RegularPolygon(Polygon):
    """A polygon that all of internal angles and side lengths are the same."""

    def __init__(self, length, sides):
        """Create a regular polygon.

        length    length of side of the polygon. (e.g., 6)
        sides     sides of the polygon. (e.g., pentagon have 5 sides)
        """
        self._sides = sides
        self._length = length

    def perimeter(self):
        return self._sides * self._length

    def area(self):
        """Return the area of polygon.

        S = p * a / 2
        p = perimeter
        a = length / (2*tan(180/sides))
        """
        area = 0.25*self._sides*self._length**2 / math.tan(math.radians(180/self._sides))
        return float('{:.2f}'.format(area))

    def __repr__(self):
        return f'length={self._length}'


class Pentagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(length, 5)


class Hexagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(length, 6)


class Octagon(RegularPolygon):
    def __init__(self, length):
        super().__init__(length, 8)


class PolygonWithCoordinates(Polygon):
    """The irregular polygon that specify the coordinates of the vertices."""

    def __init__(self, coor):
        """Create an irregular polygon

        coor    List the x and y coordinates of each vertex of the polygon in counterclockwise order
        """
        self._coordinates = coor

    def perimeter(self):
        perimeter = 0
        last = self._coordinates[-1]
        for c in self._coordinates:
            perimeter += ((c[0]-last[0])**2 + (c[1]-last[1])**2) ** 0.5
            last = c
        return float("{:.2f}".format(perimeter))

    def area(self):
        """Return the area of irregular polygon.

        [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        a = x1*y2 + x2*y3 + x3*y4 + x4*y1
        b = y1*x2 + y2*x3 + y3*x4 + y4*x1
        S = 1/2*|a-b|
        """
        area = 0
        last = self._coordinates[-1]
        for c in self._coordinates:
            area += (last[0] * c[1] - last[1] * c[0])
            last = c
        return float("{:.2f}".format(abs(area) * 0.5))

    def is_similar_with(self, other):
        """Check two polygon is similar."""

        # corresponding angles are congruent
        if self.angles != other.angles:
            return False
        # corresponding sides are proportional
        proportion = self.perimeter() / other.perimeter()
        for i in range(len(self.lengths)):
            if self.lengths[i]/other.lengths[i] != proportion:
                return False
        return True

    @property
    def lengths(self):
        """Return all lengths of side of polygon."""
        lengths = []
        last = self._coordinates[-1]
        for c in self._coordinates:
            lengths.append(((c[0]-last[0])**2 + (c[1]-last[1])**2) ** 0.5)
            last = c
        return sorted(lengths)

    @property
    def angles(self):
        """Return all angles of the polygon."""
        penult = self._coordinates[-2]
        last = self._coordinates[-1]
        angles = []
        for c in self._coordinates:
            angle = (math.atan2(penult[0]-last[0], penult[1]-last[1]) -
                     math.atan2(c[0]-last[0], c[1]-last[1]))
            angles.append(angle)
            penult, last = last, c
        return sorted(angles)

    def __repr__(self):
        return "coordinates=" + str(self._coordinates)


if __name__ == '__main__':
    t = Triangle([3, 2, 3])
    print(f'the triangle of {t}')
    print("perimeter", t.perimeter())
    print("area", t.area())
    print()

    it = IsoscelesTriangle([3, 5, 3])
    print(f'the isosceles triangle of {it}')
    print("perimeter:", it.perimeter())
    print("area:", it.area())
    print()

    et = EquilateralTriangle(4)
    print(f'the equilateral triangle of {et}')
    print("perimeter:", et.perimeter())
    print("area:", et.area())
    print()

    q = Quadrilateral([4, 4, 4, 4], [90, 90])
    print(f'the quadrilateral of ({q})')
    print("perimeter:", q.perimeter())
    print("area:", q.area())
    print()

    r = Rectangle([3, 4])
    print(f'the rectangle of ({r})')
    print('perimeter:', r.perimeter())
    print('area:', r.area())
    print()

    s = Square(5)
    print(f'the square of ({s})')
    print('perimeter:', s.perimeter())
    print('area:', s.area())
    print()

    p = Pentagon(7)
    print(f'the regular pentagon of {p}')
    print('perimeter:', p.perimeter())
    print('area:', p.area())
    print()

    h = Hexagon(9)
    print(f'the regular hexagon of {h}')
    print('perimeter:', h.perimeter())
    print('area:', h.area())
    print()

    o = Octagon(9)
    print(f'the regular octagon of {o}')
    print('perimeter:', o.perimeter())
    print('area:', o.area())
    print()

    ip = PolygonWithCoordinates([(-2, -2), (2, -2), (2, 2), (-2, 2)])
    print(f'the irregular polygon of {ip}')
    print('perimeter:', ip.perimeter())
    print('area:', ip.area())
    print()

    ip1 = PolygonWithCoordinates([(0, 0), (2, 0), (2, 2), (0, 2)])
    print('test two polygon is similar:')
    print(f'the polygon A = {ip}')
    print(f'the polygon B = {ip1}')
    print(f'the result of A ~ B:', ip.is_similar_with(ip1))

