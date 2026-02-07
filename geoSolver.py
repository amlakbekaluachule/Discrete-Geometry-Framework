class GeometryProblem:
    def __init__(self):
        self.points = []
        self.lines = []
        self.circles = []
        self.engine = ProofEngine()

    def add_point(self, P):
        self.points.append(P)

    def add_line(self, L):
        self.lines.append(L)

    def add_circle(self, C):
        self.circles.append(C)

    def solve(self):
        self.engine.run()
        return self.engine.facts
