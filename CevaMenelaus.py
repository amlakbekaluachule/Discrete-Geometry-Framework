def ratio(P, A, B):
    if not are_collinear(A, P, B):
        raise ValueError("Points not collinear")
    return distance(A, P) / distance(P, B)


def ceva_condition(A, B, C, D, E, F):
    return abs(
        ratio(D, B, C) *
        ratio(E, C, A) *
        ratio(F, A, B) - 1
    ) < EPS


def menelaus_condition(A, B, C, D, E, F):
    return abs(
        ratio(D, B, C) *
        ratio(E, C, A) *
        ratio(F, A, B) + 1
    ) < EPS


def ceva_proof(A, B, C, D, E, F):
    if ceva_condition(A, B, C, D, E, F):
        return (
            "By Ceva’s Theorem, the lines AD, BE, and CF "
            "are concurrent."
        )
    return None


def menelaus_proof(A, B, C, D, E, F):
    if menelaus_condition(A, B, C, D, E, F):
        return (
            "By Menelaus’ Theorem, points D, E, and F "
            "are collinear."
        )
    return None
