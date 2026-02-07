import math

EPS = 1e-9

class Point:
    def __init__(self, x, y, name=None):
        self.x = float(x)
        self.y = float(y)
        self.name = name or "P"

    def __repr__(self):
        return f"{self.name}({self.x}, {self.y})"


class Line:

    def __init__(self, a, b, c, name=None):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.name = name or "ℓ"

    @staticmethod
    def from_points(P, Q, name=None):
        a = Q.y - P.y
        b = P.x - Q.x
        c = -(a * P.x + b * P.y)
        return Line(a, b, c, name)

    def contains(self, P):
        return abs(self.a * P.x + self.b * P.y + self.c) < EPS


class Circle:
    def __init__(self, center, radius, name=None):
        self.center = center
        self.r = float(radius)
        self.name = name or "𝒞"

    @staticmethod
    def from_three_points(A, B, C, name=None):
        D = 2 * (A.x * (B.y - C.y) +
                 B.x * (C.y - A.y) +
                 C.x * (A.y - B.y))
        if abs(D) < EPS:
            raise ValueError("Points are collinear")

        ux = ((A.x**2 + A.y**2)*(B.y - C.y) +
              (B.x**2 + B.y**2)*(C.y - A.y) +
              (C.x**2 + C.y**2)*(A.y - B.y)) / D

        uy = ((A.x**2 + A.y**2)*(C.x - B.x) +
              (B.x**2 + B.y**2)*(A.x - C.x) +
              (C.x**2 + C.y**2)*(B.x - A.x)) / D

        center = Point(ux, uy, "O")
        r = distance(center, A)
        return Circle(center, r, name)

    def contains(self, P):
        return abs(distance(self.center, P)**2 - self.r**2) < EPS


def distance(A, B):
    return math.hypot(A.x - B.x, A.y - B.y)


def signed_area(A, B, C):
    return (
        A.x * (B.y - C.y)
        + B.x * (C.y - A.y)
        + C.x * (A.y - B.y)
    ) / 2


def are_collinear(A, B, C):
    return abs(signed_area(A, B, C)) < EPS


def collinearity_proof(A, B, C):
    if are_collinear(A, B, C):
        return (
            f"{A.name}, {B.name}, {C.name} are collinear since "
            "the signed area of triangle "
            f"{A.name}{B.name}{C.name} is zero."
        )
    return None


def directed_ratio(A, B, C):

    if not are_collinear(A, B, C):
        raise ValueError("Points not collinear")
    return distance(A, C) / distance(C, B)


def cross_ratio(A, B, C, D):
    if not (are_collinear(A, B, C) and are_collinear(A, B, D)):
        raise ValueError("Points not collinear")
    AC = distance(A, C)
    BC = distance(B, C)
    AD = distance(A, D)
    BD = distance(B, D)
    return (AC / BC) / (AD / BD)


def harmonic_proof(A, B, C, D):
    cr = cross_ratio(A, B, C, D)
    if abs(cr + 1) < EPS:
        return (
            f"The quadruple ({A.name}, {B.name}; {C.name}, {D.name}) "
            "is harmonic since the cross ratio equals −1."
        )
    return None


def are_concyclic(A, B, C, D):
    try:
        circle = Circle.from_three_points(A, B, C)
        return circle.contains(D)
    except ValueError:
        return False


def cyclicity_proof(A, B, C, D):
    if are_concyclic(A, B, C, D):
        return (
            f"Points {A.name}, {B.name}, {C.name}, {D.name} "
            "lie on a common circle."
        )
    return None


def power_of_point(P, circle):
    return distance(P, circle.center)**2 - circle.r**2


def power_proof(P, A, B, circle):
    if abs(power_of_point(P, circle) -
           (distance(P, A) * distance(P, B))) < EPS:
        return (
            f"The power of {P.name} with respect to {circle.name} "
            f"is PA·PB."
        )
    return None


def radical_axis(c1, c2):
    dx = c2.center.x - c1.center.x
    dy = c2.center.y - c1.center.y
    c = (c1.center.x**2 + c1.center.y**2 - c1.r**2
         - c2.center.x**2 - c2.center.y**2 + c2.r**2)
    return Line(2*dx, 2*dy, c, "RadicalAxis")


def are_concurrent(L1, L2, L3):
    def intersect(LA, LB):
        D = LA.a * LB.b - LB.a * LA.b
        if abs(D) < EPS:
            return None
        x = (LB.b * (-LA.c) - LA.b * (-LB.c)) / D
        y = (LA.a * (-LB.c) - LB.a * (-LA.c)) / D
        return Point(x, y)

    P = intersect(L1, L2)
    if P is None:
        return False
    return L3.contains(P)


def concurrency_proof(L1, L2, L3):
    if are_concurrent(L1, L2, L3):
        return (
            f"Lines {L1.name}, {L2.name}, {L3.name} "
            "are concurrent."
        )
    return None


A = Point(0, 0, "A")
B = Point(1, 1, "B")
C = Point(2, 2, "C")
D = Point(0, 2, "D")

print(collinearity_proof(A, B, C))
print(cyclicity_proof(A, B, C, D))
