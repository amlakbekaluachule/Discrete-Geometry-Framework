class ProjectivePoint:
    def __init__(self, x, y, z, name=None):
        self.x = x
        self.y = y
        self.z = z
        self.name = name or "P̂"

    def normalize(self):
        if abs(self.z) > EPS:
            self.x /= self.z
            self.y /= self.z
            self.z = 1


class ProjectiveLine:
    def __init__(self, a, b, c, name=None):
        self.a = a
        self.b = b
        self.c = c
        self.name = name or "ℓ̂"


def dual_point_to_line(P):
    return ProjectiveLine(P.x, P.y, P.z, f"dual({P.name})")


def dual_line_to_point(L):
    return ProjectivePoint(L.a, L.b, L.c, f"dual({L.name})")


def intersection_projective(L1, L2):
    x = L1.b * L2.c - L1.c * L2.b
    y = L1.c * L2.a - L1.a * L2.c
    z = L1.a * L2.b - L1.b * L2.a
    return ProjectivePoint(x, y, z)
